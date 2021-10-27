instance = {}


def singleton(aClass):
    global instance

    def _wrapper(*args, **kwargs):
        ret = instance.get(aClass)
        if ret is None:
            ret = aClass(*args, **kwargs)
            instance[aClass] = ret
        return ret
    return _wrapper


@singleton  # 此举保证了该类只会被初始化一次
class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("init")

    def get_age(self):
        return self.age


# class Account(object):
#     @singleton
#     def __init__(self, id, storage) -> None:
#         self.id = id
#         self.storage = storage

#     def has_storage(self):
#         return self.storage > 0


p1 = Person("Andy", 10)
p2 = Person("Bob", 12)
print(f"{p1.get_age()=}, {p2.get_age()=}")

# a1 = Account(1001, 44)
# a1 = Account(1001, 44)
"""
进一步加深了装饰器的理解 —— —— @将下面一行的定义对象传值给其后面的装饰器函数， 作为参数， 并且将输入的参数传递给调用装饰器函数返回的函数
"""
