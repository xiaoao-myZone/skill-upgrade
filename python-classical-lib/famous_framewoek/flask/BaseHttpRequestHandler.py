"""
1. https://blog.csdn.net/xhw88398569/article/details/49179967
    简单介绍HTTPServer和BaseHTTPResponseHandler的用法
2. https://blog.csdn.net/qq_35038500/article/details/87943004
    进一步介绍BaseHTTPResponseHandler
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
# import urllib
import json
# import socket
# import select
# from http.server import HTTPServer, BaseHTTPRequestHandler

socekt_map = {}
process_map = {}


class SimpleHTTPHandler(BaseHTTPRequestHandler):
    """ attr                    type            annotation
    self.command                str              GET or POST
    self.path                   str                 
    self.headers       http.client.HTTPMessage      first line
    self.raw_requestline        bytes
    self.rfile        <class '_io.BufferedReader'>  read body
    self.wfile        <class '_io.BufferedReader'>  write response
    """

    def do_GET(self):
        attr = ["command", "path", "headers", "raw_requestline", "rfile"]
        for i in attr:
            obj = getattr(self, i)
            print("%s|%s|%s" % (i, type(obj), str(obj)))

        self.send_response(200)
        # self.send_header("Content-type","text/html")
        self.send_header("Content-type", "application/json")
        self.send_header("test", "This is test!")
        self.end_headers()
        buf = json.dumps({"code": 0}).encode()
        buf += b'\n'
        self.wfile.write(buf)

    def do_POST(self):
        print(self.headers)
        data_len = int(self.headers.get("content-length"))
        if data_len:
            data = self.rfile.read(data_len)
            # TODO what if content-length is too small
            print("receive data|%s|%s" % (type(data), data))
        self.send_response(200)
        # self.send_header("Content-type","text/html")
        self.send_header("Content-type", "application/json")
        self.send_header("test", "This is test!")
        self.end_headers()
        buf = json.dumps({"code": 0}).encode()
        buf += b'\n'
        self.wfile.write(buf)


if __name__ == "__main__":
    http_server = HTTPServer(("", 7005), SimpleHTTPHandler)

    http_server.serve_forever()

"""
self.fileno()

self._handle_request_noblock()

    Handle one request, without blocking.
    
    I assume that selector.select() has returned that the socket is
    readable before this function was called, so there should be no risk of
    blocking in get_request().

        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)
        else:
            self.shutdown_request(request)

self.service_actions()

    Called by the serve_forever() loop.
    
    May be overridden by a subclass / Mixin to implement any code that
    needs to be run during the loop.

"""
