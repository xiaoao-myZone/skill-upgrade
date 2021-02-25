# -*-coding: utf-8 -*-
"""
referrence: https://www.cnblogs.com/ygbh/p/11989483.html
"""

import signal
def func(*args):
    print(args)
    print("**asf****")
print(func)
print(signal.SIGINT)
signal.signal(signal.SIGINT, func)
import time
signal.pause()
# while True:
#     time.sleep(1)
# shell 对一个进程的操作，比如kill会产生相应的响应，signal.signal创建了一个子线程去处理这个响应
"""
"""