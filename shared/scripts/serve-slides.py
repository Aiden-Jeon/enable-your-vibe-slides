"""
슬라이드 프리뷰 서버

프로젝트 루트에서 실행하면 모든 섹션의 슬라이드를 브라우저에서 확인할 수 있습니다.

실행: python shared/scripts/serve-slides.py
접속: http://localhost:8000
"""

import http.server
import os
import socketserver

PORT = 8000
DIRECTORY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 슬라이드 서버 시작: http://localhost:{PORT}")
        print(f"📁 루트 디렉토리: {DIRECTORY}")
        print()
        print("섹션별 슬라이드:")
        sections_dir = os.path.join(DIRECTORY, "sections")
        if os.path.exists(sections_dir):
            for section in sorted(os.listdir(sections_dir)):
                slide_path = os.path.join(sections_dir, section, "index.html")
                if os.path.exists(slide_path):
                    print(f"  → http://localhost:{PORT}/sections/{section}/index.html")
        print()
        print("Ctrl+C로 종료")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n서버 종료")


if __name__ == "__main__":
    main()
