import time
import asyncio
from asyncio.coroutines import iscoroutinefunction
# dir(asyncio)
"""
1. 初步来看dir(asyncio)的输出结果， asyncio存在归并threading与queue的野心
2. 或者说， asyncio可能希望， 开发者可以很方便地将原来的threading框架转化为coroutine框架
"""


async def say_something():
    for _ in range(2):
        # print(f"now it's {time.strftime('%H:%M:%S')}")
        print(f"now it's {time.strftime('%X')}")
        await asyncio.sleep(1)  # 可以注释掉
    return 0

print("say_something 是一个协程函数吗? %s" %
      ('是' if iscoroutinefunction(say_something) else '否'))
# ret = asyncio.run(say_something())
# print(f"say_something 的结果是: {ret}")
"""
1. async 与 await构成了一个协程函数
2. async函数不一定非要有await
3. asyncio.run可以运行一个协程函数
    1. 它运行时会创建一个event loop
    2. 当函数结束时， 会关闭这个loop
    3. event loop一个“线程”中只能有一个
    4. 理想情况下， python推荐我们将它作为main的入口, 并且只调用一次
"""

# 三种方式运行coroutine的机制
# run create_task


async def say_after(delay, what):
    # print("start")
    await asyncio.sleep(delay)
    print(what)


def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    loop = asyncio.get_running_loop()
    future_obj = loop.run_in_executor(
        None, blocking_io)
    # print(dir(future_obj))  也具有Task的一些方法， 比如cancle
    # 不过存在feed_data feed_eof set_exception set_transport这些令人期待的方法
    random_number = await future_obj
    print('default thread pool', random_number)

    print(f"started at {time.strftime('%X')}")
    # create_task创建后会直接运行
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # print(dir(task1))
    task1.cancel()  # 可被取消
    # await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())
"""
asyncio.sleep(0)可以作为一种暂时移交当前CPU调用权的方法， 用在长时间运行的代码片段中
"""
"""
asyncio的高级封装API
1. 并发执行协程并且控制它们
2. 执行IO和IPC（进程间通信）
3. 控制子进程（不就是进程间通信?）
4. 同步并发代码(不太懂？)
asyncio的低级封装API
1. 创建病管理evelt loop
"""

"""
参考资料：
    1. https://docs.python.org/3/library/asyncio.html
"""
