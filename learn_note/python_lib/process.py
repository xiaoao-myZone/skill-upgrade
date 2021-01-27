#-*- coding: utf-8 -*-
from multiprocessing import Process, Queue
#from queue import Queue

def product(q):
    #global q
    var = 1
    # q.put(var)
    print("put %s in queue" % var)

def consume(q):
    #global q
    ret = q.get()
    print("get % in queue" % ret)


q = Queue(5)
p1 = Process(target=product, args=(q,))
p1.start()
p2 = Process(target=consume, args=(q,))
p2.daemon = False
p2.start()





"""
Conclusion:
    1. 将queue.Queue的实例以参数传入Process，貌似不会联动，但是两个Queue的id是一样的，这个比较费解
    2. Pipe实例化时创建了一个server socket和一个client socket
    3. multiprocessing.Queue无论是作为全局变量还是参数传入时都可以实现其功能
    4. TODO 探究multiprocessing.Queue的机理，看是否可以用在两个主进程之间
"""