# -*- coding: utf-8 -*-
def ask_again():
    def _wrapper(func):
        def __wrapper(self, *args, **kwargs):
            print(args)
            print(kwargs)
            ret = func(self, *args, **kwargs)
            if ret:
                ret = False
            return ret
        return __wrapper

    return _wrapper


@ask_again()
def func_a(self=0, times=4):
    print("self: %d" % self)
    return True


# __wrapper只能接受调用函数时输入的参数,不能无法获得在定义函数时默认的函数参数
print(func_a(0, 3))
