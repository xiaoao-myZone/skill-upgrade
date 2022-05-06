1. 在python3中Exception无法涵盖KeyBoardException
2. python3中的字典遍历顺序就是k-v对添加的顺序, 但是在字典使用k-v初始化的过程中，不能保证实际得到的字典的k-v顺序按照代码书写顺序(对吗？)[python3字典有序还是无序_无序字典和有序字典](https://blog.csdn.net/weixin_39520210/article/details/110380884) python3.7及以后字典变为有序，体现在：一，遍历字典的key有序， 调用dict::keys dict::values dict::items 均获得有序的可迭代对象
3. dict_obj.fromkeys(iterable, value=None)会返回一个新字典，这个新字典只受iterable和value的影响，与dict_obj没有关系
