#!/usr/bin/env python3
import sys
import socket
import select


def server(port=7005):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    epoll = select.epoll()
    s.bind(("", port))
    s.listen(4)
    conn, addr = s.accept()
    epoll.register(conn)
    events = epoll.poll()
    print("first poll: %s" % str(events))
    data = conn.recv(5)
    print("data: %s" % data)
    events = epoll.poll()
    print("second poll: %s" % str(events))
    data = conn.recv(5)
    print("data: %s" % data)
    epoll.unregister(conn)
    events = epoll.poll(2)
    print("third poll: %s" % str(events))
    s.close()

def client(port=7005):
    c = socket.socket()
    c.connect(("", 7005))
    data = b"abcdefghijklmnopqrst"
    c.send(data)
    print("send: %s" % data)
    c.recv(1024)

if __name__ == "__main__":
    choice, *others= sys.argv[1:]
    if not others:
        port = others[0]
    else:
        port = 7005
    if choice == "client":
        client(port=port)
    elif choice == "server":
        server(port=port)