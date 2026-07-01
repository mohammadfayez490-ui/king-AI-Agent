from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AstraMindServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {
                "system": "AstraMind",
                "status": "running"
            }

            self.wfile.write(json.dumps(response).encode())


    def do_POST(self):
        if self.path == "/chat":
            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length)

            request = json.loads(data)

            message = request.get("message", "")

            response = {
                "message": message,
                "reply": "AstraMind Agent is ready"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())


server = HTTPServer(
    ("0.0.0.0", 8000),
    AstraMindServer
)

print("AstraMind Backend Running")

server.serve_forever()
