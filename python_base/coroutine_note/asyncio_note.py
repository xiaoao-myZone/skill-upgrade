#!/usr/bin/python3
import time
import asyncio
"""
1. async await 用法  https://www.cnblogs.com/xinghun85/p/9937741.html
2. async的库         https://www.cnblogs.com/shenh/p/9090586.html   
3. 专业的理解         https://blog.csdn.net/permike/article/details/110821246

"""
"""
    异步编程就是无法预知执行时间的计算机程序
"""


async def lucky_num(i):
    await asyncio.sleep(1)  # 关键是并没有sleep
    print("my lucky num is : %s:%d" % (str(int(time.time()*1000))[-2:], i))
    # print(time.time())


def run():
    for i in range(10):
        loop.run_until_complete(lucky_num(i))


loop = asyncio.get_event_loop()


if __name__ == "__main__":
    run()
    # print(type(lucky_num))

"""
1. await 会挂起一个协程对象,并且不会被阻塞,继续执行后面的代码
2. async 将一个函数或者方法申明为协程对象
3. asyncio.get_event_loop()返回一个循环池对象,这个对象可以添加协程对象,然后在一个循环中去处理这些协程
"""


