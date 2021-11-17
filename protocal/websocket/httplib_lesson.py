from http.server import BaseHTTPRequestHandler

# CGI (common gateway interface)
print(dir(BaseHTTPRequestHandler))

url = "http://127.0.0.1:500/api/cmd/test"
