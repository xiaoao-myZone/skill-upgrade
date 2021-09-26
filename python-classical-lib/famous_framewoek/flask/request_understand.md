[1. Referrence](https://www.cnblogs.com/MnCu8261/p/10013702.html)
[2. Referrence](https://www.cnblogs.com/minsons/p/8251780.html) socketio详解
[3. flask请求流程详解](https://www.bbsmax.com/A/A7zg68LPd4/)
[4. Flask基础框架入门*推荐*](https://www.bilibili.com/video/BV19V411H7qH)

1. 在Local的实例中， 每个线程都映射一个stack， 这个stack是一个list， 如果每个线程对应一个请求， 那么这个list显然是多余的
2. 除非， flask有一个参数限制线程池的数量
