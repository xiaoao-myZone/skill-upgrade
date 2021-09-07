from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib, base64
import struct
import time
import json

MAGIC_STRING = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
HOST = "127.0.0.1"
PORT = "7006=5"
HANDSHAKE_STRING = "HTTP/1.1 101 Switching Protocols\r\n" \
            "Upgrade:websocket\r\n" \
            "Connection: Upgrade\r\n" \
            "Sec-WebSocket-Accept: {1}\r\n" \
            "WebSocket-Location: ws://{2}/chat\r\n" \
            "WebSocket-Protocol:chat\r\n\r\n"


class SimpleHTTPHandler(BaseHTTPRequestHandler):
    """ attr                    type            annotation
    self.command                str              GET or POST
    self.path                   str                 
    self.headers       http.client.HTTPMessage      first line
    self.raw_requestline        bytes
    self.rfile        <class '_io.BufferedReader'>  read body
    self.wfile        <class '_io.BufferedReader'>  write response
    """
    is_ws = False
    def do_GET(self):
        # attr = ["command", "path", "headers", "raw_requestline", "rfile"]
        # for i in attr:
        #     obj = getattr(self, i)
        #     print("%s|%s|%s" % (i, type(obj), str(obj)))

        if "Sec-WebSocket-Key" in self.headers:
            self.deal_ws()
            return

        self.send_response(200)
        #self.send_header("Content-type","text/html")
        self.send_header("Content-type","application/json")
        self.send_header("test","This is test!")
        self.end_headers()
        buf = json.dumps({"code": 0}).encode()
        buf+=b'\r\n'
        self.wfile.write(buf)

    def do_POST(self):
        print(self.headers)
        data_len = int(self.headers.get("content-length"))
        if data_len:
            data = self.rfile.read(data_len)
            print("receive data|%s|%s" % (type(data), data))
        self.send_response(200)
        #self.send_header("Content-type","text/html")
        self.send_header("Content-type","application/json")
        self.send_header("test","This is test!")
        self.end_headers()
        buf = json.dumps({"code": 0}).encode()
        buf+=b'\r\n'
        self.wfile.write(buf)
    
    def deal_ws(self):
        sec_key = self.headers['Sec-WebSocket-Key'] + MAGIC_STRING
        res_key = base64.b64encode(hashlib.sha1(sec_key.encode()).digest()).decode()
        str_handshake = HANDSHAKE_STRING.replace('{1}', res_key).replace('{2}', HOST + ':' + str(PORT))
        self.send_response(101)
        self.send_header("Upgrade", "websocket")
        self.send_header("Connection", "Upgrade")
        self.send_header("Sec-WebSocket-Accept", res_key)
        # TODO more
        # buf=b'\r\n' # TODO neccesary?
        # self.wfile.write(buf)
        self.server.is_ws = True
        self.is_ws = True
        print("deal_ws")
        from ipdb import set_trace; set_trace()
    
class ReliableServer(HTTPServer):
    is_ws = False
    def _handle_request_noblock(self):
        self.is_ws = False
        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                return self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)
        else:
            self.shutdown_request(request)


    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        if self.is_ws:
            return request
        self.shutdown_request(request)

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    def service_actions(self):
        # TODO deal http request
        pass

import select

epoll = select.epoll()
http_server = ReliableServer(("127.0.0.1", 7005), SimpleHTTPHandler)
http_server_fd = http_server.fileno()
server_sock = http_server.socket

epoll.register(http_server_fd)

socket_map = {}
socket_map[http_server_fd] = server_sock
ws_set = set()



def add_socket(conn):
    global socket_map
    global epoll
    fd = conn.fileno()
    socket_map[fd] = conn
    epoll.register(fd)

def remove_socket(fd):
    global socket_map
    global epoll
    conn = socket_map.pop(fd)
    epoll.unregister(fd)
    conn.close()

def read(fd):
    global socket_map
    conn = socket_map.get(fd)
    datas = []
    while True:
        data = conn.recv(4096)
        if data:
            datas.append(data)
        else:
            break
    return b"".join(datas).decode()

def send_ws(fd, data):
    global socket_map
    global epoll
    conn = socket_map.get(fd)
    # TODO python3将字符转换为bytes后长度会变化吗
    length = len(data)
    token = b"\x81"
    if length < 126:
        token += struct.pack("B", length)
    elif length <= 0xFFFF:
        token += struct.pack("!BH", 126, length)
    else:
        token += struct.pack("!BQ", 127, length)
    
    data = b"".join((token, data.encode()))
    conn.sendall(data)
    epoll.modify(fd, select.EPOLLIN)
    

while True:
    events = epoll.poll(1)
    if not events:
        continue
    for fd, event in events:
        if fd == http_server_fd:
            print("有新连接")
            ws = http_server._handle_request_noblock()
            if ws:
                add_socket(ws)
                ws_set.add(ws.fileno())

        elif event & select.EPOLLIN:
            recv_data = read(fd)
            print(recv_data)
        
        elif event & select.EPOLLOUT:
            send_ws(fd, str(time.time()))
        elif event & select.EPOLLHUP:
            remove_socket(fd)
        
        else:
            print("{fd}: unknown event {event}".format(fd, event))

            
