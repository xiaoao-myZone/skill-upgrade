# -*- coding: utf-8 -*-
"""
1. https://www.cnblogs.com/34fj/p/6358702.html
   # 对int这类不可变的类的继承,以及单例模式的实现
"""
class Test(object):
   def __init__(self, arg):
      self.name = arg
   
   def printf(self):
      print(self.name)

t = Test("kunkun")
print(t.__class__)
m = t.__class__("qunqun")
m.printf()