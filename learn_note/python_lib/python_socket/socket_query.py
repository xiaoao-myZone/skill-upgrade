import socket
addr = socket.gethostbyname("www.baidu.com")
print(addr) #--> 36.152.44.95
name = socket.gethostbyaddr(addr)
print(name)