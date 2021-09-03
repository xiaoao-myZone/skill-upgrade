class A(object):
    def __init__(self):
        print("This is A")


class B(A):
    def __init__(self):
        print("This is B")
        # super(A, self).__init__()
        super(B, self).__init__()


b = B()


"""
Conclusion:
    1. 继承一个类就拥有了调用这个类中所有方法的能力
    2. 当继承者与被继承者都有某一个方法时,默认用继承者的,这叫做"改写"
    3. 当想使用被继承者的方法,同时这个方法已经在继承者中被定义时(TODO 不是改写吗？),就需要借助super
    4. 因为当前类的__init__重写了被继承类的init，所以后者的init要被执行， 只能借助super
    5. self.__class__.mro是一个列表,存放着自己以及各级被继承的类,可以看做继承历史记录
    6. super的实质
        def super(cls, inst):
            mro = inst.__class__.mro()
            return mro[mro.index(cls) + 1]
    7. super并非只能在__init__中写
"""


class TestA(object):
    def __init__(self):
        print("keyword")
        self.value = 33

    def handle(self):
        print("handle something")

    def report(self):
        print(self.value)


class TestB(TestA):
    def tick(self):
        print("tick")

    def handle(self):
        print("B handle")


class TestC(TestB):
    def __init__(self):
        # pass
        super().__init__()  # python2.7需要写成super(BaseClass, self).__init__()

    def knock(self):
        print("knock")


c = TestC()
c.tick()
c.knock()
c.handle()
c.report()
# report 用到了在基类的__init__过程中定义的self.value， 但是新类C重写了__init__，
# 导致c.report()报错AttributeError

