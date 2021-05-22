# -*- coding: utf-8 -*-
from imp import reload
import hot_import
while True:
    ans = input("enter to continue")
    if not ans:
        reload(hot_import)
        from hot_import import data
        print(data)
    else:
        break



"""
Conclusion:
    1. 当hot_import中所读的json文件被修改时， 在不重启进程的情况下， import是不会再执行hot_import.py中的内容的
    2. 需要调用reload， 但是入reload好像只有python2有
    3. python3中reload在imp这个lib里

"""