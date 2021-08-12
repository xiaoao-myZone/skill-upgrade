class Dog:
    legs = 4
    def __init__(self, name):
        self.name = name

xiaohua = Dog("xiaohua")
wangcai = Dog("wangcai")
print(Dog.legs)


print("legs of xiaohua is %s" % xiaohua.legs)
print("legs of wangcai is %s" % wangcai.legs)

xiaohua.legs = 6
print("")
print("legs of xiaohua is %s" % xiaohua.legs)
print("legs of wangcai is %s" % wangcai.legs)


Dog.legs = 7
print("")
print("legs of xiaohua is %s" % xiaohua.legs)
print("legs of wangcai is %s" % wangcai.legs)




"""
Conclusion:
    1. 当实例给类属性赋值后， 类改变类属性，对该实例不起作用， 在这之前可以起作用
    2. 可以用作用域的概念去理解， 类属性在外层， 实例属性在里层， 前者像global, 后者像local
    3. 相对应的cls是代表类属性的作用域， self代表实例的作用域， self继承了cls


静态方法， 类方法与实例方法的理解
https://blog.csdn.net/magicharvey/article/details/20217357

1. 静态方法：无法访问类属性、实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已。
2. 类成员方法：可以访问类属性，无法访问实例属性。上述的变量val1，在类里是类变量，在实例中又是实例变量，所以容易混淆。 

静态属性
https://blog.csdn.net/Mr_Slower/article/details/83662923?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162872787316780271598841%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=162872787316780271598841&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-83662923.first_rank_v2_pc_rank_v29&utm_term=python+%E9%9D%99%E6%80%81%E5%B1%9E%E6%80%A7%E4%BF%AE%E6%94%B9&spm=1018.2226.3001.4187

"""


class Cat:
    def __init__(self) -> None:
        self.ears = 2
    
    @staticmethod
    def move():
        print("moving")

    @staticmethod
    def move():
        print("moving")
    
    @classmethod
    def roll(cls):
        print("rolling")

    @classmethod
    def roll(cls):
        print("rolling")
    

    def mew(self):
        print("I'm %s" % name)

    def mew(self):
        pass

"""一些错误（重复的方法名）不会被检查出来， 或者说被覆盖了"""