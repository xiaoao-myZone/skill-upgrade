"""
1. https://blog.csdn.net/xhw88398569/article/details/49179967 简单介绍HTTPServer和BaseHTTPResponseHandler的用法
2. https://blog.csdn.net/qq_35038500/article/details/87943004 进一步介绍BaseHTTPResponseHandler
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        print(path)
        #拆分url(也可根据拆分的url获取Get提交才数据),可以将不同的path和参数加载不同的html页面，或调用不同的方法返回不同的数据，来实现简单的网站或接口
        # query = urllib.parse.splitquery(path)
        # print(query)
        self.send_response(200)
        #self.send_header("Content-type","text/html")
        self.send_header("Content-type","application/json".encode())
        self.send_header("test","This is test!".encode())
        self.end_headers()
        buf = json.dumps({"code": 0}).encode()
        self.wfile.write(buf)

server = HTTPServer(("", 7005), MyHandler)
from ipdb import set_trace; set_trace()
server.serve_forever()

"""
self._handle_request_noblock()

    Handle one request, without blocking.
    
    I assume that selector.select() has returned that the socket is
    readable before this function was called, so there should be no risk of
    blocking in get_request().

self.service_actions()

    Called by the serve_forever() loop.
    
    May be overridden by a subclass / Mixin to implement any code that
    needs to be run during the loop.

"""