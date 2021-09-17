"""
wrapper会改变func的__name__等属性
"""

from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrapper


def log_without_wrap(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return wrapper


@log_without_wrap
def hello1():
    print("hello")
    return 1


@log
def hello2():
    print("hello")
    return 1


print(hello1.__name__)  # 输出 wrapper
print(hello2.__name__)  # 输出 hello2
