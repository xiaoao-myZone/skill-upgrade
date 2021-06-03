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
b = TestB()
a = TestA()
print(isinstance(c, TestB))
print(isinstance(c, TestA))
print(isinstance(b, TestC))
print(isinstance(b, TestA))
print(isinstance(a, TestC))
print(isinstance(a, TestB))

print("-"*10)
print(issubclass(a.__class__, TestB))

"""
Conclusion:
    isinstance会通过 ins.__class__.mro()返回的列表查找cls是否在其中
"""