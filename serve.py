"""极简静态服务器，绕开 http.server.HTTPServer 的 getfqdn 中文主机名编码 bug。"""
import http.server
import socketserver
import functools
import os

DIR = os.path.dirname(os.path.abspath(__file__))
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)


class QuietTCPServer(socketserver.TCPServer):
    # 用 TCPServer 而非 HTTPServer：HTTPServer.server_bind 会调 socket.getfqdn，
    # 中文 Windows 主机名下抛 UnicodeDecodeError，这里直接跳过。
    allow_reuse_address = True


if __name__ == "__main__":
    PORT = 8000
    with QuietTCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Serving at http://127.0.0.1:{PORT}  (Ctrl+C 退出)")
        httpd.serve_forever()
