##this creates simple server listener on port 8000 for practicing ##

from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"hello World")

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Running on port 8000...")
server.serve_forever()
