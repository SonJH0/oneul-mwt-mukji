// ===== 다크모드 =====
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// 저장된 테마 불러오기
if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark');
    themeToggle.textContent = '☀️';
}

// 버튼 클릭 시 전환
themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    
    if (body.classList.contains('dark')) {
        themeToggle.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    } else {
        themeToggle.textContent = '🌙';
        localStorage.setItem('theme', 'light');
    }
});
