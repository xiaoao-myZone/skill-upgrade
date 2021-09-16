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


b = base()
print(b.__dict__)  # __dict__只保存实例的属性
b.x = 10  # 我才知道一个类可以在实例化之后如此任意地创建一个新的属性
print(b.__dict__)
