class Test(object):
    def __init__(self):
        return 1


c = Test()
print(c)

"""
Conclusion:
    1. init只能返回None，否则会出现TypeError
"""
