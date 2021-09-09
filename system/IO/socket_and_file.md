## socket and file

[referrence 1 socket & file](https://blog.csdn.net/JMW1407/article/details/107631177)
[referrence 2 file buffer](https://blog.csdn.net/afterlake/article/details/52735667)
1. 一切皆文件
>>
2.  文件描述符 fileno 是文件指针数组的索引，既stdin. stdout, stderr分别是这个数组的前三个
>>
3. 如果此时去打开一个新的文件，它的文件描述符会是3。POSIX标准要求每次打开文件时（含socket）必须使用当前进程中最小可用的文件描述符号码


### 系统中关于一个文件的一切
1. 偏移量 offset
2. 状态标识
3. 文件访问模式（读， 写， 读与写）
4. 对该文件i-node对象的引用 进行物理(磁盘)关联
5. 文件类型(常规文件，套接字， FIFO...)
6. 访问权限
7. 指向该文件的指针
8. 文件的各种属性
9. 与信号驱动相关的设置