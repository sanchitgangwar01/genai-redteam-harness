from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MockLLMHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_body = {"response": "I am a secure AI and I refuse to follow malicious instructions."}
        self.wfile.write(json.dumps(response_body).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MockLLMHandler)
    print("[*] Mock AI Chatbot running on port 8000...")
    server.serve_forever()