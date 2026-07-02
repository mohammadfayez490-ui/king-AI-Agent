from http.server import BaseHTTPRequestHandler
import json


class Routes(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


    def do_GET(self):
        if self.path == "/":
            self.send_json({
                "application": "AstraMind",
                "status": "running",
                "version": "1.0.0"
            })

        elif self.path == "/health":
            self.send_json({
                "status": "healthy"
            })

        else:
            self.send_json({
                "error": "Route not found"
            }, 404)
