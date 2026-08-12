import google.generativeai as genai
import os
import json

# ===== Gemini API 설정 =====
# 환경변수에서 키 가져오기 (안전!) 🔐
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")


# ===== Vercel Serverless 함수 =====
def handler(request):
    # OPTIONS 요청 처리 (CORS)
    if request.method == "OPTIONS":
        return _response({}, 200)

    # POST 요청만 허용
    if request.method != "POST":
        return _response({"error": "POST만 가능해요"}, 405)

    try:
        # 1. JS에서 보낸 데이터 받기
        data = request.get_json()
        mood = data.get("mood", "")
        food = data.get("food", "")
        food_custom = data.get("foodCustom", "")
        people = data.get("people", "")

        # 빈 입력 체크! (실패 처리)
        if not mood and not food and not food_custom:
            return _response({"error": "조건을 선택해주세요!"}, 400)

        # 2. AI에게 물어볼 질문 만들기
        prompt = f"""
        너는 친절한 음식 추천 전문가야.
        아래 조건에 맞는 메뉴 1개를 추천해줘.

        - 기분: {mood}
        - 원하는 음식 종류: {food}
        - 직접 입력한 음식: {food_custom}
        - 인원: {people}

        형식:
        1. 추천 메뉴 이름
        2. 추천 이유 (2~3문장, 친근하게)

        이모지도 적절히 써줘! 😊
        """

        # 3. AI에게 물어보고 답 받기
        response = model.generate_content(prompt)
        result = response.text

        # 4. JS에게 답 돌려주기
        return _response({"result": result}, 200)

    except Exception as e:
        # API 오류 처리 (실패 처리)
        return _response({"error": "잠시 후 다시 시도해주세요!"}, 500)


# ===== 응답 만드는 도우미 함수 =====
def _response(body, status):
    return {
        "statusCode": status,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps(body, ensure_ascii=False)
    }