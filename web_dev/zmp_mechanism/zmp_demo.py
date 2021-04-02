#-*- coding: utf-8 -*-

import random, threading, time, zmq
B = 32

# TOOD random.getrandbits lstrip
# lstrip = leading strip
def ones_and_zeros(digits):
    return bin(random.getrandbits(digits)).lstrip("0b").zfill(digits)

def bitsource(zcontext, url):
    zsock = zcontext.socket(zmq.PUB)
    zsock.bind(url)
    while True:
        zsock.send_string(ones_and_zeros(B * 2))
        time.sleep(0.01)

def always_yes(zcontext, in_url, out_url):
    # 不是很懂为啥有个无选择性的发送'Y'
    # 因为订阅的是00
    # 这里就有个疑问, 00开头只能说点落在边长比原正方形小1的正方形内,怎么能说一定在圆内呢
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    # 和socket一样,虽然发送的str,但是接收到的是bytes
    isock.setsockopt(zmq.SUBSCRIBE, b'00')
    # 00开头一定在圆内?
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        isock.recv_string()
        osock.send_string('Y')

def judge(zcontext, in_url, pythagoras_url, out_url):
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    for prefix in b'01', b'11', b'10':
        isock.setsockopt(zmq.SUBSCRIBE, prefix)
    psock = zcontext.socket(zmq.REQ) # TODO what's REQ
    psock.connect(pythagoras_url)
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    unit = 2 ** (B * 2) # 圆的半径的平方
    while True:
        bits = isock.recv_string()
        # 这里是二进制, 少一位, 长度直接缩一半
        n, m = int(bits[::2], 2), int(bits[1::2], 2)
        psock.send_json((n, m)) #这是元组吧, 能以json格式发吗?
        sumsquares = psock.recv_json()
        osock.send_string('Y' if sumsquares < unit else 'N')

def pythagoras(zcontext, url):
    zsock = zcontext.socket(zmq.REP)
    zsock.bind(url)
    while True:
        numbers = zsock.recv_json()
        zsock.send_json(sum(n * n for n in numbers)) # 点到原点距离的平方

def tally(zcontext, url):
    zsock = zcontext.socket(zmq.PULL)
    zsock.bind(url)
    p = q = 0
    while True:
        decision = zsock.recv_string()
        q += 1
        if decision == 'Y':
            p += 4
        print(decision, p / q)

def start_thread(function, *args):
    thread = threading.Thread(target=function, args=args)
    thread.daemon = True
    thread.start()

def main(zcontext):
    pubsub = 'tcp://127.0.0.1:6700'
    reqrep = 'tcp://127.0.0.1:6701'
    pushpull = 'tcp://127.0.0.1:6702'
    start_thread(bitsource, zcontext, pubsub)
    start_thread(always_yes, zcontext, pubsub, pushpull)
    start_thread(judge, zcontext, pubsub, reqrep, pushpull)
    start_thread(pythagoras, zcontext, reqrep)
    start_thread(tally, zcontext, pushpull)
    time.sleep(30)

if __name__ == "__main__":
    main(zmq.Context())

"""
1. zcontext是上下文,它维护者一个队列
2. bitsource生成随机序列, 使用zmq.PUB发布
3. 存在两种订阅,通过zmq.SUB获取订阅通道, 通过zmq.SUBSCRIBE订阅种类(信息开头)
4. 订阅后将判定结果通过zmq.PUSH发送
5. tally函数将发送的结果通过zmq.PULL收集, 进行统计
6. 不以00开头的序列将送给judge函数来判断, 通过zmq.REQ发送, 通过zmq.REP接受

总结:
1. 在本例中zmq创建了三种信道
2. PUSH-PULL    生产消费模型        单向一对一
3. PUB-SUB      发布订阅模型        单向一对多
4. REQ-REP      类似http的C-S结构   双向多对一


"""