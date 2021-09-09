#-*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import time
#from queue import Queue

def product(q):
    #global q
    var = 1 #[1] #product
    q.put(var)
    print("put %s in queue" % var)

def consume(q):
    #global q
    ret = q.get()
    print("get %s in queue, type: %s" % (ret, type(ret)))


# q = Queue(5)
# p1 = Process(target=product, args=(q,))
# p1.start()
# p2 = Process(target=consume, args=(q,))
# p2.daemon = False
# p2.start()


# TODO Pipe Queue Manager分别能接受什么数据类型
# queue貌似接受的数据类型挺多,函数也可以传qvq
print("--------------Pipe-------------")
from multiprocessing import Pipe
def product_P(q):
    var = 2 #[1] #product
    q.send(var)
    time.sleep(0.2)
    q.send(3)
    print("put %s in queue")

def consume_P(q):
    time.sleep(1)
    while True:
        ret = q.recv()
        print("get %s in queue, type: %s" % (ret, type(ret)))

r_p, w_p = Pipe()
p1 = Process(target=product_P, args=(r_p,))
p1.start()
print("pid: %d" % p1.pid)
p2 = Process(target=consume_P, args=(w_p,))
print("default daemon is %s" % p2.daemon)
p2.start()
print("pid: %d" % p2.pid)




"""
Conclusion:
    1. 将queue.Queue的实例以参数传入Process，貌似不会联动，但是两个Queue的id是一样的，这个比较费解
    2. Pipe实例化时创建了一个server socket和一个client socket
    3. multiprocessing.Queue无论是作为全局变量还是参数传入时都可以实现其功能
    4. TODO 探究multiprocessing.Queue的机理，看是否可以用在两个主进程之间
"""