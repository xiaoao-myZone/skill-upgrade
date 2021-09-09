## TCP/IP
1. [三次握手与四次挥手](https://blog.csdn.net/qq_43412060/article/details/107140216?utm_source=app&app_version=4.5.4)
    ![三次握手示意图](https://img-blog.csdnimg.cn/2020070811151980.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDEyMDYw,size_16,color_FFFFFF,t_70)
    * SYN表示这次通讯的目的是为了同步,也就是建立连接
    * ACK表示这次通讯是为了回答上一次对方的通讯
    * ack对上一次的seq加一,标志了所回答的询问(这与JD提供的报文规则貌似不一样,它的ack没有对seq加一)
    * 每次一个通讯都加上自己的seq,并且从SYN后(初始化seq),每次通讯就递增自己的seq

2. 与socket的联系 
    * listen: 告诉linux内核套接字与已连接的套接字的队列长度[listen参考](https://www.cnblogs.com/fnlingnzb-learner/p/8523508.html)
    * accept: 将队列中完成连接的socket从队列中移出
    * connect: 通知Linux内核,与服务器socket建立三次握手
    * 与connect作用的是listen而不是accept
    * 未连接队列一般为256,已连接队列根据listen的参数,一般不超过30
    * 如果任何一个队列满了,connect应该会阻塞
    

3. 半连接(正确应答了一次,但是没有应答第二次)
    * 服务端只应答了第一次,客户端已经建立了连接
    * 客户端最后一次没有应答
    * 断开连接有一方没有应答

4. 三次握手的正义性
    * 两次握手,如果客户端第一次的握手在到达服务端建立连接前(可能是传输时间过长,可能是服务器处理前面的队列时间过久),已失效(客户端等待syn超时,放弃,或者序列号本身有时间限制?),那么服务器将白白建立起一个无效的连接

5. 四次挥手
![](https://img-blog.csdnimg.cn/20200708141954478.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDEyMDYw,size_16,color_FFFFFF,t_70)

6. 半断开(按照图示应该有三种情况)

7. close与shutdown
    * close只是将当前应用程序与socket断开联系
    * socket本质上是通过内核来维护的
    * 内核是否会去检查有无应用程序使用某一socket,如果都没有该如何处理(回收)?


### SYN攻击
[socket握手SYN和ACK理解](https://blog.csdn.net/weixin_30512043/article/details/99777669)
### 疑问
1. 那么如果后一个队列满了会怎么样?
2. 发起握手的随机序列号是否可能相同?
3. 