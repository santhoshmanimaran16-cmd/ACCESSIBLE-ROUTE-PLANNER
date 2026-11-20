"""One-click launcher: serves the app on http://localhost so maps, address
search and GPS work. Works on Windows / macOS / Linux. Needs only Python 3."""
import http.server, socketserver, webbrowser, os, sys, threading

HERE = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(HERE, "Original Implementation")
if ".zip" in HERE.lower() or not os.path.isfile(os.path.join(APP_DIR, "index.html")):
    sys.exit(
        "\nThe app files were not found next to this script.\n"
        "You are most likely running it from INSIDE the zip file.\n"
        "Fix: close this, right-click the .zip -> Extract All, open the extracted\n"
        "folder, and run start_app.py (or the START HERE file) from there.\n")
os.chdir(APP_DIR)
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True
for port in range(PORT, PORT + 20):
    try:
        httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)
        break
    except OSError:
        continue
else:
    sys.exit("No free port found (8000-8019). Close other servers and retry.")
url = f"http://localhost:{port}/index.html"
print(f"Running at {url}  (press Ctrl+C to stop)")
threading.Timer(1.0, lambda: webbrowser.open(url)).start()
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nStopped.")
