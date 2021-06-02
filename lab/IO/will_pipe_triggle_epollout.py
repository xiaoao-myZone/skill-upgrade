#-*- coding: utf-8 -*-
import os
import select
from multiprocessing import Process
from threading import Thread
"""
1: EPOLLIN
2: EPOLLPRI
4: EPOLLOUT
8: EPOLLERR
16: EPOLLHUP
"""
epoll = select.epoll()
r, w = os.pipe()
print("r: %d, w: %d" % (r, w))
epoll.register(r)
epoll.register(w)
print(epoll.poll(0.5)) # w一直触发EPOLLOUT事件
epoll.modify(w, select.EPOLLIN)
print(epoll.poll(0.1)) # modify后就没有了
# w = os.fdopen(w, "w", 0) #can't set unbuffered
f_w = os.fdopen(w, "w", 1)
f_r = os.fdopen(r, "r", 1)
f_w.write("hello\n") #w的写触发r的EPOLLIN
print(epoll.poll(0.5)) 
print(f_r.readline(), end="")

def read(f_r):
    print(print(f_r.readline(), end=""))
thread = Process(target=read, args=(f_r,))
thread.start()
print(epoll.poll(0.5)) # r管道进入阻塞地读,并不能触发w的任何事件
thread.terminate()

# thread = Process(target=read, args=(f_w,)) # w不能进行读操作
# thread.start()
# print(epoll.poll(0.5))

# os.close(w)
# print(epoll.poll(0.5)) # 关闭w,r会出现EPOLLHUP事件
os.close(r)
print(epoll.poll(0.5)) # 关闭r, w会出现EPOLLERR事件

"""
Conclusion:
    1. w一直触发EPOLLOUT事件
    2. w的写触发r的EPOLLIN
    3. r管道进入阻塞地读,并不能触发w的任何事件
    4. 关闭w,r会出现EPOLLHUP事件
    5. 关闭r, w会出现EPOLLERR事件

Notes:
    1. 管道不能设置为unbuffered,也就是os.fdopen最后参数需要大于0
    2. w不能包装成file object进行读操作,估计任何O操作都不行(output)
    3. epoll对EPOLLIN的监听， 本质上是查询缓存区是否有数据， 所以如果一次没有接受完缓存， 调用poll的时候依然有该描述符的EPOLLIN信号
    4. unregister一个文件对象后， 即便这个socket没有关闭， poll的结果中也不会有它（3， 4可以从epoll_regitset.py中得到印证）
"""
