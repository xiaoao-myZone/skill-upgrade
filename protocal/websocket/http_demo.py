"""
referrence:
    1. https://blog.csdn.net/wuchuanpingstone/article/details/82964256

Questions:
    1. 如何处理并发? ---> epoll
    2. 如何将客户端发来的信息全部接受?
    3. 如何在重启server后,不出现端口不可用的情况?
    4. epollout是什么事件?
"""

import select
import socket
import traceback

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1", 7006))
server.listen(5)
server.setblocking(False)


epoll = select.epoll()
server_fd = server.fileno()
socket_map = {server_fd: server}
epoll.register(server_fd)

def recv(conn, type="GET"):
    ret = []
    try:
        while True:
            data = conn.recv(4096, socket.MSG_DONTWAIT)
            if data:
                data = data.decode("utf-8")
            else:
                break
            ret.append(data)
    except BlockingIOError:
        pass
    return ''.join(ret)

def unregister(epoll, socket_map, fd):
    socket_map[fd].close()
    epoll.unregister(fd)
    del socket_map[fd]
    print("close")


try:
    while True:
        events = epoll.poll(2)
        if not events:
            print("waiting....")
            continue
        print("events", events)
        for fd, event in events:
            if fd == server_fd:
                conn, addr = server.accept()
                print("#### %s:%s connected####" % addr)
                _fd = conn.fileno()
                #conn.setblocking(False)
                socket_map[_fd] = conn
                epoll.register(_fd)
            
            elif event & select.EPOLLIN:
                conn = socket_map[fd]
                data = recv(conn)
                # TODO parse http
                print("&&&&& receive data: \n%s" % data)
                if not data:
                    unregister(epoll, socket_map, fd)
                else:
                    # TODO switch return
                    ret = [
                        "HTTP/1.1 200 OK\r\n",
                        "content-type: application/json\r\n",
                        "\r\n",
                        '{"code": 0, "msg": "success", "data": {}}'
                    ]
                    try:
                        conn.send("".join(ret).encode("utf-8"))
                    except BrokenPipeError:
                        print("already closed")
                    #conn.close()
                
            
            elif event & select.EPOLLHUP:
                conn = socket_map[fd]
                print("#### %s:%s disconnected####" % conn.getpeername())
                epoll.unregister(fd)
                del socket_map[fd]
            
            elif event & select.EPOLLOUT:
                conn = socket_map[fd]
                epoll.modify(conn, select.EPOLLIN)
                print("#### %s:%s modified####" % conn.getpeername())
except :
    traceback.print_exc()
server.close()
            
        
"""
1. REST Client发过来的报文:
GET / HTTP/1.1
user-agent: vscode-restclient
content-type: : application/json
accept-encoding: gzip, deflate
Host: 127.0.0.1:7006
Connection: close

2. Postman发来的报文:
GET / HTTP/1.1
User-Agent: PostmanRuntime/7.26.3
Accept: */*
Postman-Token: 7673885a-5e06-4293-9a17-ec4a4ed3ebd2
Host: 127.0.0.1:7006
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

3. 浏览器发来的报文:
GET / HTTP/1.1
Host: 127.0.0.1:7006
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1



Conclusion:
    1. http请求的结束信号应该是收到的字符数据结尾是"/r/n/r/n"
    2. 基本上所有的客户端的socket连接后,都会在服务端epoll这边触发读事件
"""