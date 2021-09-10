"""
https://www.cnpython.com/qa/156358
https://stackoverflow.com/questions/53356451/pyzmq-high-water-mark-not-working-on-pub-socket/53360536#53360536
http://api.zeromq.org/
http://api.zeromq.org/master:zmq-setsockopt
"""
import zmq
import sys
import time


def subscribe(url, sub):

    ctx = zmq.Context()
    client = ctx.socket(zmq.SUB)
    
    # 第二个参数只能是0或1,设置为1后, 貌似只能订阅最后一个(按字母顺序排序)
    # conflate: 合流
    # 这个需要在connect之前设置才有效
    # client.setsockopt(zmq.CONFLATE, 1)
    # option to get the last message only which defined in subscriber side.
    # 上一句话来自第二个链接

    client.setsockopt(zmq.RCVHWM, 1)
    client.setsockopt(zmq.RCVBUF, 1)
    for prefix in sub:
        client.setsockopt(zmq.SUBSCRIBE, prefix.encode())
    if not sub:
        client.setsockopt(zmq.SUBSCRIBE, "".encode())
    
    client.connect(url)
    while True:
        # print("-------------")
        # data = input()
        # print("input: %s" % data)
        data = client.recv_string()
        print(data)
        time.sleep(0.1)

if __name__ == "__main__":
    url = sys.argv[1]
    sub = sys.argv[2:]
    print("sub: %s" % str(sub))
    print("subscribe...")
    subscribe(url, sub)


