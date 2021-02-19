def log(func):
    def _wrapper(self, *args, **kwargs):
        print("Class: %s" % self.__class__)
        print("function: %s" % func.__name__)
        print(' '.join(map(str,args)))
        print(" ".join(["{key}: {value}".format(key=key, value=value) for key, value in kwargs.items()]))
        ret=func(self, *args, **kwargs)
        print(ret)
        return ret

    return _wrapper

class Test(object):
    def __init__(self):
        pass
    
    @log
    def add(self, a, b):
        return a+b

t = Test()
t.add(1, 5)
