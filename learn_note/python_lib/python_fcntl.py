#-*- coding: utf-8 -*-
import fcntl
"""
一般用来给文件加锁
referrence: https://zhangnq.com/3284.html
    https://blog.csdn.net/farsight2009/article/details/55517833

1. 复制一个现有的描述符(cmd=F_DUPFD).

2. 获得/设置文件描述符标记(cmd=F_GETFD或F_SETFD).

3. 获得/设置文件状态标记(cmd=F_GETFL或F_SETFL).

4. 获得/设置异步I/O所有权(cmd=F_GETOWN或F_SETOWN).

5. 获得/设置记录锁(cmd=F_GETLK , F_SETLK或F_SETLKW).
"""
fcntl.F_GETFL
print(fcntl.F_GETFL)
import sys
flags = fcntl.fcntl(sys.stderr.fileno(), fcntl.F_GETFL, 0)
print(flags)