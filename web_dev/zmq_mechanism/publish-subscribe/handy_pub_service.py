import sys, zmq

def hand_pub(url):
    ctx = zmq.Context()
    server = ctx.socket(zmq.PUB)
    server.setsockopt(zmq.SNDHWM, 1)
    server.setsockopt(zmq.SNDBUF, 1)
    server.bind(url)
    print("server start...")
    while True:

        data = input()
        server.send_string(data)
        print("send: %s" % data)

if __name__ == "__main__":
    url = sys.argv[1]
    hand_pub(url)