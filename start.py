import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    Handler = MyHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server đang chạy tại http://localhost:{PORT}")
        print("Mở trình duyệt của bạn và truy cập:")
        print(f"http://localhost:{PORT}/index.html")

        webbrowser.open_new_tab(f"http://localhost:{PORT}/index.html")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer đã dừng.")

if __name__ == "__main__":
    run_server()
