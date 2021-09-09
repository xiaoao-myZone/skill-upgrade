"""
一文搞懂什么是Python的metaclass
https://zhuanlan.zhihu.com/p/98440398

1. metaclass就是type，类的定义其实就是调用class_obj = type(class_name, superclasses, attrs)
其中class_name是str, superclasses是元组, attrs是属性与类方法

2. 在上述过程中， type会对
"""