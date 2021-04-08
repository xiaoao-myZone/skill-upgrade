# -*- coding: utf-8 -*-
"""
Conclusion:
    1. python2.7对内源性的中文支持是可以的
    2. python2.7对外源性的中文处理起来很麻烦, 比如给使用flask框架的服务器发送夹杂中文的json, 
        如果不用json.dumps输出就会比较麻烦,容易乱码
    3. 

"""
import json
a = {"data": "上山打老虎"}
print(str(a))
print(a["data"])