import http.server

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'text/html')
        super().end_headers()

http.server.test(HandlerClass=MyHTTPRequestHandler)
