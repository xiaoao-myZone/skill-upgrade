### Threading Lib of Python

#### Thread
1. 线程为守护进程时，会与主进程供一起结束
2. 线程只是为了异步编程，将一个任务分给多个线程来做，速度不见得会快
3. 若要提升效率，可以采用协程(coroutine)与多进程(process)，因为这两者可以使用多核

#### Event
1. set, is_set, clear, wait四种主要方法