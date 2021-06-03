getattr
setattr


def switch(func):
    def _wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        print("from wrapper", getattr(self, func.__name__))
        return ret

    return _wrapper

class Demo(object):
    def __init__(self, name):
        self.name = name
    @switch
    def func(self):
        print("my name is %s" %self.name)


d = Demo("xiaoming")
print(getattr(d, 'name'))
setattr(d, "name", "xiaofang")
print(getattr(d, 'name'))
print("-------------------------")
print(getattr(d, 'func')) # TODO 找出为什么这一句为什么莫名其妙打印出<bound method switch.<locals>._wrapper of <__main__.Demo object at 0x7f9dcb56bb00>>
d.func()

