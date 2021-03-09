import time
import sys
import subprocess
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado import gen
from tornado.options import define, options, parse_command_line

define("port", default=8888, type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        title1 = ''
        try:
            title1 = self.get_argument("text1")
        except:
            self.render("ws_tornado.html", textDiv="")
        if title1:
            self.render("ws_tornado.html", textDiv="textDiv")

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self, *args):

        pass

    def on_message(self, message):

        import time
        from collections import deque

        def tail(filename, n=10):
            'Return the last n lines of a file'
            while True:
                lines = '<br>'.join(list(deque(open(filename), n)))
                self.write_message(lines)
                if lines:
                    time.sleep(0.5)
                    continue
        tail('ip.txt')

    def on_close(self):
        print("Connection closed")


app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/text1', IndexHandler),
    (r'/ws', WebSocketHandler),
])


if __name__ == '__main__':
    #from ipdb import set_trace; set_trace()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()