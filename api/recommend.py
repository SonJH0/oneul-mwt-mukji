from http.server import BaseHTTPRequestHandler
from google import genai
import os
import json

# ===== Gemini API 설정 =====
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# ===== Vercel Serverless 함수 =====
class handler(BaseHTTPRequestHandler):

    # CORS 처리
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    # POST 요청 처리
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            mood = data.get("mood", "")
            food = data.get("food", "")
            food_custom = data.get("foodCustom", "")
            people = data.get("people", "")

            if not mood and not food and not food_custom:
                self._send_json({"error": "조건을 선택해주세요!"}, 400)
                return

            # 사용 가능한 모델 확인!
            model_names = []
            for m in client.models.list():
                model_names.append(m.name)

            self._send_json({"result": str(model_names)}, 200)

        except Exception as e:
            self._send_json({"result": str(e)}, 500)

    # 응답 만드는 도우미 함수
    def _send_json(self, body, status):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(body, ensure_ascii=False).encode('utf-8'))
