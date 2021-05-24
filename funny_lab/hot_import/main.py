# -*- coding: utf-8 -*-
from imp import reload
import hot_import

def print_data():
    print(data)


while True:
    ans = input("enter to continue")
    if not ans:
        reload(hot_import)
        from hot_import import data
        global data
        # print(data)
        print_data()
    else:
        break



"""
Conclusion:
    1. 当hot_import中所读的json文件被修改时， 在不重启进程的情况下， import是不会再执行hot_import.py中的内容的
    2. 需要调用reload， 但是入reload好像只有python2有
    3. python3中reload在imp这个lib里
    4. reload后需要重新import
    5. reload对象可以是一个包， 也可以是包下面的一个模块， 或者一个单纯的模块
    6. logger重载后， 会打印出多倍的日志

"""