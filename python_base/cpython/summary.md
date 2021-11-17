[Python 为什么这么慢？](https://blog.csdn.net/chinesehuazhou2/article/details/90746215)
* GIL: 多线程在同一个核上
* 垃圾回收
* 编译: 预编译为opcode， 存在pyc或者__pycahce__中, opcode转换成机器语言指令需要时间, 虚拟机， java同样有JIT， 但是不慢， 是因为做了很多优化, 需要大量财力， 另外是有了JIT启动会比较慢
* 动态语言: 意味着解释器需要自己判断变量的类型