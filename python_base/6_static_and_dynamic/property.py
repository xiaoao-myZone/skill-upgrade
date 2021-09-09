class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def cal1(self):
        return self.a + self.b

    @cal1.setter  # 利用此方法设置静态属性
    def cal1(self, value):
        print('hahaha', self, value)
        self.__dict__['cal1'] = value  # 直接操作字典,避免无限递归

    @cal1.getter  # 调用属性时触发,触发条件只与实例有关
    def cal1(self):
        print('get is running')
        return self.a + self.b

    @cal1.deleter
    def cal1(self):  # 删除静态属性时触发
        print('deleter is running')
        self.__dict__.pop('cal1')

t = Test('love', 'you')
print(t.cal1)
print(Test.cal1)     # 输出的是一个property对象
t.cal1 = 'sa'        # 而实例不可设置静态属性,除非有setter
#Test.cal1 = 'happy'  # 类可以设置静态属性
print(t.__dict__)
del t.cal1
print(t.__dict__)
# ————————————————
# 版权声明：本文为CSDN博主「Mr_Slower」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Mr_Slower/article/details/83662923