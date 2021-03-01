import os
import select

r, w = os.pipe()
# try:
#     os.fdopen(w, "r", 1) #
# except Exception as e:
#     print(e)
try:
    os.fdopen(r, "w", 1) #
except Exception as e:
    print(e)
epoll = select.epoll()
epoll.register(r, select.EPOLLIN)
print("first time", epoll.poll(0.5))
os.close(w)
print("second time", epoll.poll(0.5))

"""
Conclusion:
    1. os.pipe返回的应该是两个指向同一个文件的描述符,通过某种设置,将前后两个文件描述符分别限定了只能用读的模式打开与只能用写的模式打开
    2. os.fdopen如果以不恰当的模式打开fd,会关闭此fd
    3. os应该有办法提前得知这种读写模式限定
    4. 当文件写入的一端关闭后,读的一端应该被永久写入了EOF,并且每次都触发epoll的EPOLLHUB事件
"""


