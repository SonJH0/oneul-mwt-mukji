# 🍽️ 오늘 뭐 먹지?

AI가 당신의 기분과 상황에 맞는 메뉴를 추천해주는 웹 서비스입니다.

## 📖 서비스 소개

"오늘 뭐 먹지?"는 매일 반복되는 메뉴 고민을 
AI가 대신 해결해주는 서비스입니다.

오늘의 기분, 원하는 음식 종류, 인원수를 선택하면
Gemini AI가 딱 맞는 메뉴를 추천해줍니다!

## ✨ 주요 기능

- 😊 기분 선택 (행복/우울/스트레스/피곤)
- 🍜 음식 종류 선택 (한식/중식/일식/양식)
- ✍️ 직접 음식 입력 가능
- 👥 인원수 선택 (혼밥/여럿이서)
- 🤖 AI 맞춤 메뉴 추천

## 🛠️ 기술 스택

**프론트엔드**
- HTML
- CSS
- JavaScript

**백엔드**
- Python (Vercel Serverless Functions)

**AI**
- Google Gemini API (gemini-2.0-flash)

**배포**
- Vercel
- GitHub

## 🌐 배포 URL

https://oneul-mwt-mukji.vercel.app

## 🚀 실행 방법

### 1. 저장소 클론
\`\`\`bash
git clone https://github.com/SonJH0/oneul-mwt-mukji.git
cd oneul-mwt-mukji
\`\`\`

### 2. 환경 변수 설정
프로젝트 루트에 \`.env\` 파일을 생성하고 
아래 내용을 입력하세요.

\`\`\`
GEMINI_API_KEY=your_api_key_here
\`\`\`

### 3. Vercel 배포
- GitHub 저장소를 Vercel에 연결
- Vercel 대시보드에서 환경 변수 등록
  - Key: \`GEMINI_API_KEY\`
  - Value: 발급받은 API 키

## 🔑 환경 변수

| 변수명 | 설명 |
|--------|------|
| \`GEMINI_API_KEY\` | Google Gemini API 키 |

> ⚠️ API 키는 절대 코드에 직접 입력하지 마세요!
> 반드시 환경 변수로 관리하세요.

## 📁 폴더 구조

<img width="309" height="267" alt="image" src="https://github.com/user-attachments/assets/bacb1416-a20d-478b-a5f1-5b64c981ed31" />



## 👤 제작자

- SonJH0
