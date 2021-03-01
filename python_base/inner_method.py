getattr
setattr


def switch(func):
    def _wrapper(self, *args, **kwargs):
        ret = func(self, *args, **kwargs)
        print(getattr(self, func.__name__))
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
print(getattr(d, 'func'))
d.func()

