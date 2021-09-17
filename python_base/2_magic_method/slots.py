"""
python __slots__ 详解（上篇）
    https://blog.csdn.net/sxingming/article/details/52892640
"""


class base(object):
    var = 9

    def __init__(self):
        pass

    def print(self):
        print("hello, world!")


a = base()
print(a.__dict__)  # __dict__只保存实例的属性， 而没有实例的方法
a.x = 10  # 我才知道一个类可以在实例化之后如此任意地创建一个新的属性
print(a.__dict__)

print('*'*30)


class base_slot(object):
    __slots__ = 'x'
    # x = 7  # 这样x将会成为只读属性

    def __init__(self):
        pass


b = base_slot()
try:
    print(b.__dict__)
except AttributeError:
    print("there is no __dict__")
try:
    b.y = 7
except AttributeError:
    print("can't add attr that is not in __slot__")
b.x = 20
print(f'{b.x=}')
print(dir(b))

print('*'*30)


# def get_id():
#     return random.randint(0, 1000)


class Local(object):
    __slots__ = ('__storage__', '__ident_func__')

    def __init__(self, get_id):
        object.__setattr__(self, '__storage__', {})
        object.__setattr__(self, '__ident_func__', get_id)

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}


def get_id_a():
    return 1


def get_id_b():
    return 2


a = Local(get_id_a)
# print(a.__storage__)  # {}
a.key = 'XX'
print(a.__storage__)
b = Local(get_id_b)
# print(b.__storage__)
b.value = "ss"
print(b.__storage__)
print(a.__ident_func__)

"""
Conclusion:
    1. slots是为类的实例共享了若干个属性
"""
