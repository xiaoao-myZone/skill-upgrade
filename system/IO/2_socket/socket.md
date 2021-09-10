## socket

1. 如果一对socket对象中， 一方的send已经调用结束， 而另一方的recv还在等待， 则接受方会报错socket.error: [Errno 11] Resource temporarily unavailable
2. 照理说不应该出现这种情况， 这是因为将blocking设置为false 
3. 当socket调用bind和listen(n)后， 客户端即可connect
4. 但是当未被accept的连接达到n+1时， 接下来的connect会被阻塞
5. settimeout可以以抛出异常（socket.timeout）的方式结束connect, accept和recv的阻塞
6. 将settimeout设置为None, 相当于setblocking(1)
7. 将settimeout设置为0, 相当于setblocking(0)

### key point
1. 系统有独立的进程来处理缓存区的数据
2. 数据会被分成小的数据包， 并且加上源网卡地址与目的网卡地址，以及消息序列
3. 如果在指定时间内（这个时间大概是多少）没有收到ack， 会重传

### question
1. 什么是滑动窗口?(当对方读的速度赶不上写的速度时)
2. 当收到对方ack后， 写入缓存才会删掉， 而缓存如果打包成很多个小包， 是收到所有小包才会删除，还是收到一个？我觉得是前者， 这样数据传输才会可靠
3. 一个数据包的大小是多少？[UDP中一个包的大小最大能多大？TCP呢？](https://blog.csdn.net/qq_39382769/article/details/95701854)
* TCP/IP的数据传输都是基于以太网的帧（72-1526）， 去掉以太网的头部信息26字节后， 数据帧在46-1500之间
* TCP/IP也有头部信息， 其中TCP头部数据为20字节， UDP头部数据为8字节， 我猜主要差在包的序号上
4. 什么是滑动窗口？ [【技术控】详解TCP之滑动窗口](https://www.zhihu.com/search?type=content&q=%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%20tcp)
* 发送端接收到一个包的ack后，滑动窗口就会向右移动
* 发送端一次会发多个序号连续的包，数量取决于系统性能， 体现在参数window_size
* 接收端只有在最前面的包接收到后， 才会发送这个包的ack， 后面的包即便提前收到， 也不会发送
* 每次发送ack，接收端都会检查窗口从左连续收到的包中， 最右的那个包的ack, 这叫累计确认原则
* 窗口大小不能大于序号空间的一半， 否则收发端窗口不能完全对齐
5. 什么是拥塞控制？
* 拥塞控制是发送端通过数据发出到响应的时间来判断网络拥塞程度, 拥塞窗口控制sender向connection传输数据的速率，使这个速率为网络拥堵状况的函数


## referrence
[1 我们在读写Socket时，究竟在读写什么（动态图解）](https://zhuanlan.zhihu.com/p/250788944)
[2 errno 11](https://blog.csdn.net/u012203437/article/details/47297727)
