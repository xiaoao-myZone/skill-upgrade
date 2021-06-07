"""
1. https://blog.csdn.net/jerrism/article/details/107357541
"""
#from ipdb import set_trace; set_trace()
from types import MethodType
from functools import partial


class Demo(object):
    def __init__(self, name):
        self.name = name
    
    def make_introduction(self):
        print("Hi~, I'm %s" % self.name)

def new_make_intro(self):
    print("Welcome to my world, I'm %s" % self.name)

d = Demo("Judy")
d.make_introduction()

setattr(d, "name", "WolfGang")
d.make_introduction()

d.make_introduction = MethodType(new_make_intro, d)
d.make_introduction()


def switch(func):
    def _wrapper(self, *args, **kwargs):
        print("$$$step into wrapper")
        ret = func(self, *args, **kwargs)
        if not self.times:
            self.make_introduction = MethodType(new_make_intro, self)
        return ret

    return _wrapper

class Test(object):
    def __init__(self, name):
        self.name = name
        self.times = 1

    @switch
    def make_introduction(self):
        self.times-=1
        print("Hi~, I'm %s" % self.name)

    def init(self):
        #self  = self.__class__(self.name) # don't work
        self.__init__(self.name)
        self.make_introduction = MethodType(self.__class__.make_introduction, self)


print("----------------------------------")
test = Test("Dylon")
test.make_introduction()
test.make_introduction()
test.make_introduction()
print("----------------------------------")

test.init()
print(test.times)
test.make_introduction()
test.make_introduction()
print(test.times)
"""
就这个test实例而言,它的make_introduction已经被永久地改变了, 调用这个实例的__init__是没有用的
"""
print("----------------------------------")
test = Test("Dylon")
test.make_introduction()
test.make_introduction()
test.make_introduction()
"""
还好并不影响原来的类的正常使用
"""
