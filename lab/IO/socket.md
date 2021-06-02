## socket

1. 如果一对socket对象中， 一方的send已经调用结束， 而另一方的recv还在等待， 则接受方会报错socket.error: [Errno 11] Resource temporarily unavailable
2. 照理说不应该出现这种情况
3. 当socket调用bind和listen(n)后， 客户端即可connect
4. 但是当未被accept的连接达到n+1时， 接下来的connect会被阻塞
5. settimeout可以以抛出异常（socket.timeout）的方式结束connect, accept和recv的阻塞
6. 将settimeout设置为None, 相当于setblocking(1)
7. 将settimeout设置为0, 相当于setblocking(0)