#-*- coding: utf-8 -*-
class TaskPlanner(object):
    def __init__(self, name):
        self.name = name
        print("name is %s" % name)
    
    def __del__(self):
        print("%s was deleted" % self.name)
        del self # TODO del 方法是否调用了self.__del__,在这里岂不是无穷迭代


tp = TaskPlanner("Judy")
tp = TaskPlanner("Lucid")

"""
先创建新的对象,再删除旧的对象
"""