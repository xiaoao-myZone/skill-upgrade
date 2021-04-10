# -*- coding: utf-8 -*-
"""
Conclusion:
    1. python2.7对简单的str对象的处理是正常的（或者说是内部自洽的），但是对复杂结构中如果有中文就会处理不好
    2. python2.7的字符串存在两种对象str和unicode， str可以使二进制编码
    3. python3全面使用utf-8
    4. 代码中定义的中文，可以被decode("utf-8")解码成unicode, 也就是说，这个str对象其实是二进制码,在很多实用场景中python2.7自动帮我们转化了

"""
import json
print("\n")

a = {"data": "上山打老虎"}
print(str(a))
print(a["data"])
from ipdb import set_trace; set_trace()
# print(json.dumps(a, ensure_ascii=False))
print(json.dumps(a))

print("\n")

# a["data"] = a.pop("data").decode("utf-8")
# print(str(a))
print(json.loads(json.dumps(a, ensure_ascii=False))) # json.loads会将所有的str变为unicode


