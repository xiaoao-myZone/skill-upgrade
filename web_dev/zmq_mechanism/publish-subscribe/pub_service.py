import sys, zmq
import time

def hand_pub(url):
    ctx = zmq.Context()
    server = ctx.socket(zmq.PUB)
    server.setsockopt(zmq.SNDHWM, 1)
    server.setsockopt(zmq.SNDBUF, 1)
    server.bind(url)
    n = 0
    left = True
    data = input()
    while True:

        
        # server.send_string(data)
        time.sleep(0.01)
        # data = str(time.time())
        if left:
            data = "left XXXXXXXXX%10dXXXXXXXXX" % n
        else:
            data = "rightXXXXXXXXX%10dXXXXXXXXX" % n
        left = not left
        server.send_string(data)
        print("send: %s" % data)
        n+=1

if __name__ == "__main__":
    url = sys.argv[1]
    hand_pub(url)