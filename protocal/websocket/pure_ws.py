import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import 
import urllib3

class MyHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        # try:
        #     self.handle()
        # finally:
        #     self.finish()
        #     pass

    def do_GET(self):
        #self.rfile
        cookie = self.headers["Cookie"]
        parsed_path = urllib3.util.parse_url(self.path)
        query_pair = [segment.split("=") for segment in parsed_path.query.split("&")]
        query_dict = {k:v for k, v in query_pair}
        if "sid" not in query_dict:
            self.fisrt_response()
    
    def fisrt_response(self):

        self.send_response(200)
        self.send_header("Set-Cookie", "%s; path=/; SameSite=Lax" % cookie)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("'Content-Length", "119")
        self.send_header()   
        

ADDR = "127.0.0.1"
PORT = 7005
# http_server = HTTPServer((ADDR, PORT), BaseHTTPRequestHandler)
# ser_sock = http_server.socket
ser_sock = socket.socket()
ser_sock.bind((ADDR, PORT))
ser_sock.listen(1)
ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ser_fd = ser_sock.fileno()
# from ipdb import set_trace; set_trace()
epoll = select.epoll()
epoll.register(ser_fd)
reply = []
tmp = []

while True:
    events = epoll.poll()
    for fd, event in events:
        if fd == ser_fd:
            print("connect")
            request, addr = ser_sock.accept()
            epoll.register(request.fileno())
        elif event & select.EPOLLOUT:
            if reply:
                epoll.motify(fd, select.EPOLLIN)
            else:
                request.sendall(reply.pop().encdoe())
        elif event & select.EPOLLIN:
            data = request.recv(4096).decode()
            print(data)
            reply.append(tmp.pop())
            epoll.motify(fd, select.EPOLLOUT)

