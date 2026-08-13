// ===== 1. 버튼 클릭 선택 기능 =====

// 같은 그룹 안에서 하나만 선택되게 하는 함수
function setupButtonGroup(selector) {
  const buttons = document.querySelectorAll(selector);  // 해당 버튼들 모두 찾기
  
  buttons.forEach(function(btn) {           // 각 버튼마다
    btn.addEventListener("click", function() {   // 클릭되면
      buttons.forEach(b => b.classList.remove("selected")); // 형제들 선택 해제
      btn.classList.add("selected");        // 나만 선택!
    });
  });
}

// 세 그룹에 각각 적용
setupButtonGroup(".mood-btn");     // 기분 버튼
setupButtonGroup(".food-btn");     // 음식 버튼
setupButtonGroup(".people-btn");   // 인원 버튼

// ===== 2. 선택한 값 가져오기 =====

// 선택된 버튼의 값을 찾는 함수
function getSelectedValue(selector) {
  const selected = document.querySelector(selector + ".selected");  // selected 붙은 버튼 찾기
  return selected ? selected.dataset.value : "";  // 있으면 값, 없으면 빈칸
}

// "메뉴 추천 받기" 버튼 찾기
const submitBtn = document.getElementById("submit-btn");

// 버튼 클릭했을 때!
submitBtn.addEventListener("click", function() {
  // 각 선택값 가져오기
  const mood = getSelectedValue(".mood-btn");        // 기분
  const food = getSelectedValue(".food-btn");        // 음식
  const people = getSelectedValue(".people-btn");    // 인원
  
  // 자유 입력값도 가져오기
  const foodCustom = document.getElementById("food-custom").value;    // 음식 직접입력
  const peopleCount = document.getElementById("people-count").value;  // 인원수 직접입력

  // 확인용으로 화면에 띄우기!
      // 확인용 alert는 이제 안 써요! → 서버로 보내기!

    // 결과 화면에 "생각중..." 표시
    const resultBox = document.getElementById("result");
    resultBox.innerHTML = "🤔 AI가 메뉴를 고민하는 중...";

    // 서버로 데이터 보내기! (fetch)
    fetch("/api/recommend", {
      method: "POST",                          // 보내는 방식
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({                   // 데이터를 포장!
        mood: mood,
        food: food,
        foodCustom: foodCustom,
        people: people
      })
    })
      .then(response => response.json())        // 답변 받기
            .then(data => {
        resultBox.style.display = "block";   
        resultBox.innerHTML = data.result;
      })
      .catch(error => {                         // 에러 나면
        resultBox.innerHTML = "😢 오류가 생겼어요. 다시 시도해주세요!";
        console.log(error);
      });
  });
