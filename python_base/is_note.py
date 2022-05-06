"""
is 来判断变量是否为None很方便,但是在判断整数的时候好像不怎么稳定
"""
# ref: https://blog.csdn.net/qq_26442553/article/details/82195061
"""
注意，因为python对小整数在内存中直接创建了一份，不会回收，所有创建的小整数变量直接从对象池中引用他即可。
但是注意Python仅仅对比较小的整数对象进行缓存（范围为范围[-5, 256]）缓存起来，而并非是所有整数对象。
也就说只有在这个[-5,256]范围内创建的变量值使用is比较时候才会成立。
"""

"""
注意：上面对于python小整数对象池的使用仅仅是在命令行中执行可以，而在Pycharm或者保存为文件执行，结果是不一样的，
这是因为解释器做了一部分优化。下面使用pycharm,即使整数超过256，使用is也是成立的。
"""


"""
## python3的字典的有序性
1. 其顺序就是k-v对添加的顺序, 但是在字典使用k-v初始化的过程中，不能保证实际得到的字典的k-v顺序按照代码书写顺序(对吗？)
2. [python3字典有序还是无序_无序字典和有序字典](https://blog.csdn.net/weixin_39520210/article/details/110380884) python3.7及以后字典变为有序，体现在：一，遍历字典的key有序， 调用dict::keys dict::values dict::items 均获得有序的可迭代对象
3. dict_obj.fromkeys(iterable, value=None)会返回一个新字典，这个新字典只受iterable和value的影响，与dict_obj没有关系
"""

"""
enumerate循环中不能执行改动列表长度的操作，index永远是增加的，直到大于或等于当前列表长度
"""
ls = [2,4,6,8,0]
for index, i in enumerate(ls):
	if i%2==0:
		del ls[index]
print(ls) # [4, 8]


"""

"""
