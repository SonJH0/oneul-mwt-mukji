from http.server import BaseHTTPRequestHandler
from google import genai
import os
import json

# ===== Gemini API 설정 =====
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# ===== Vercel Serverless 함수 =====
class handler(BaseHTTPRequestHandler):
    
    # CORS 처리 (OPTIONS 요청)
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    # POST 요청 처리
    def do_POST(self):
        try:
            # 1. JS에서 보낸 데이터 받기
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            mood = data.get("mood", "")
            food = data.get("food", "")
            food_custom = data.get("foodCustom", "")
            people = data.get("people", "")
            
            # 빈 입력 체크
            if not mood and not food and not food_custom:
                self._send_json({"error": "조건을 선택해주세요!"}, 400)
                return
            
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
            response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
)
            result = response.text
            
            # 4. JS에게 답 돌려주기
            self._send_json({"result": result}, 200)
            
        except Exception as e:
            self._send_json({"error": "잠시 후 다시 시도해주세요!"}, 500)
    
    # 응답 만드는 도우미 함수
    def _send_json(self, body, status):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode('utf-8'))
