# -*- coding: utf-8 -*-
"""
referrece: https://blog.csdn.net/thirstyblue/article/details/7763403
"""
import os, sys
import time
r, w = os.pipe()
pid = os.fork() # 子线程与主线程共用管道,包括sys
if not pid:
    print("child process")
    print("r --> %d, w --> %d" % (r, w))
    for i in range(5):
        time.sleep(1)
        print("%d time" % i)
    # print("child process")
    # os.dup2(w, 1)
    # os.dup2(r, 0)
    # print("yes")
    # s = os.read(r, 1024)
    # time.sleep(5)
    # with open("/home/xyz/xiaoao/skill-upgrade/text.txt", "w") as f:
    #     f.write(s)
else:
    print("main thread")
    print("r --> %d, w --> %d" % (r, w))
    os.waitpid(pid, 0)

    