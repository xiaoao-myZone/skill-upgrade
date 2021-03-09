"""
1. https://www.cnblogs.com/huchong/p/8613308.html
2. 
"""
import os
import select
for i in dir(select):
    if i.startswith("EPOLL"):
        num = getattr(select, i)
        print("%s ---> %d ----> %s" % (i, num, bin(num)[2:]))


"""
POLLIN 	读取来自文件描写叙述符的数据
POLLPRI 	读取来自文件描写叙述符的紧急数据
POLLOUT 	文件描写叙述符的数据已准备好。可无堵塞写入
POLLERR 	与文件描写叙述符有关的错误情况
POLLHUP 	挂起，连接丢失
POLLNVAL 	无效请求，连接没有打开

EPOLLERR ---> 8 ----> 1000
EPOLLET ---> 2147483648 ----> 10000000000000000000000000000000
EPOLLHUP ---> 16 ----> 10000
EPOLLIN ---> 1 ----> 1
EPOLLMSG ---> 1024 ----> 10000000000
EPOLLONESHOT ---> 1073741824 ----> 1000000000000000000000000000000
EPOLLOUT ---> 4 ----> 100
EPOLLPRI ---> 2 ----> 10
EPOLLRDBAND ---> 128 ----> 10000000
EPOLLRDNORM ---> 64 ----> 1000000
EPOLLWRBAND ---> 512 ----> 1000000000
EPOLLWRNORM ---> 256 ----> 100000000
EPOLL_CLOEXEC ---> 524288 ----> 10000000000000000000
"""

print("-------------------------------")

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
try:
    epoll.register(r, select.EPOLLIN)
    print("first time", epoll.poll(0.5))
    os.close(w)
    print("second time", epoll.poll(0.5))
except Exception as err:
    print(err)



"""
Conclusion:
    1. os.pipe返回的应该是两个指向同一个文件的描述符,通过某种设置,将前后两个文件描述符分别限定了只能用读的模式打开与只能用写的模式打开
    2. os.fdopen如果以不恰当的模式打开fd,会关闭此fd
    3. os应该有办法提前得知这种读写模式限定
    4. 当文件写入的一端关闭后,读的一端应该被永久写入了EOF,并且每次都触发epoll的EPOLLHUB事件
"""

# TODO 什么情况下会触发select.EPOLLOUT? 我猜是当另一端调用recv或者read的时候

print("-----------select.select------------------")
import socket
client_1 = socket.socket()
client_1.connect(("127.0.0.1", 7005))
client_2 = socket.socket()
client_2.connect(("127.0.0.1", 7005))
rl = [client_1.fileno()]
wl = [client_2.fileno()]
xl = [client_1.fileno()]
while True:
    r, w, e = select.select(rl, wl, xl, 2)
    print(r, w, e)
    ans = input("recv?")
    if ans:
        if ans=="q" or ans=="Q":
            client_1.close()
            client_2.close()
            break
        else:
            print(client_1.recv(1024).decode())


"""server.py"""
# if True:
#     import socket
#     s = socket.socket()
#     s.bind(("127.0.0.1", 7005))
#     s.listen(3)
#     conn, addr = s.accept()

"""
Conclusion for select.select:
    1. socket通信过程中,只会收到EPOLLIN与EPOLLOUT
    2. 在server_socket收到连接时, 连接收到信息时, 对端连接调用close, 对端连接调用shutdown(socket.SHUT_WR)时,触发EPOLLIN
    3. 连接建立后会一直触发EPOLLOUT, 第一必须将其select.modify(conn, epoll.EPOLLIN),之后如果它发来信息会触发EPOLLIN
    4. 在连接EPOLLIN事件的处理中,如果select.modify(conn, epoll.EPOLLOUT)估计会回到一直触发EPOLLOUT的状态
    5. 当使用epoll处理管道时,写入端的管道关闭会触发EPOLLHUP,但是没有EPOLLOUT

Conclusion for select.select:
    1. 像select.epoll一样,既可以接受含有fileno()方法的对象,也可以接受fd
    2. 一个fd不能既放在rl里,又放在wl里, 只有w会返回fd,r一直没有
    3. 放在wl里貌似一直都会有事件
    4. xl不知道有什么作用,同时放在rl与xl中没有问题
    5. 如果rl中的另一端被关闭了,读到的信息为''
    
"""
# TODO 可否通过fcntl来得知fd的另一端是否被关闭
#应该不行

"""
Notes:
    select poll epoll的性能依次增强,但是兼容性select最好
"""