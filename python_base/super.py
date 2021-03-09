class A(object):
    def __init__(self):
        print("This is A")


class B(A):
    def __init__(self):
        print("This is B")
        #super(A, self).__init__()
        super(B, self).__init__()

b = B()

"""
Conclusion:
    1. 继承一个类就拥有了调用这个类中所有方法的能力
    2. 当继承者与被继承者都有某一个方法时,默认用继承者的,这叫做"改写"
    3. 当想使用被继承者的方法,同时这个方法已经在继承者中被定义时,就需要借助super
    4. self.__class__.mro是一个列表,存放着自己以及各级被继承的类,可以看做继承历史记录
    5. super的实质
        def super(cls, inst):
            mro = inst.__class__.mro()
            return mro[mro.index(cls) + 1]
"""

class TestA(object):
    def __init__(self):
        print("keyword")

    def handle(self):
        print("handle something")

class TestB(TestA):
    def tick(self):
        print("tick")

class TestC(TestB):
    def knock(self):
        print("knock")

c = TestC()