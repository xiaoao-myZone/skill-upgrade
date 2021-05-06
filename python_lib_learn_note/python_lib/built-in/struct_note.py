# -*- coding: utf-8 -*-
"""
1. https://blog.csdn.net/qq_30638831/article/details/80421019
"""

"""
1. 按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,不能传输int,此时先将int转化为字节流,然后再发送;
2. 按照指定格式将字节流转换为Python指定的数据类型;
3. 处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二进制(字节流)写,读的方式来处理文件;
4. 处理c语言中的结构体;

5. 如果如3, 4所说, 可以用python来解析很多媒体文件

"""
"""
# 将python中的一个正整数变为C/C++中的无符号整数
>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24 #在32位排列中, 取整数的前8位, 看是不是1, 然后去掉后面的24位, 获取前八位的值
>>> b2 = (n & 0xff0000) >> 16   #在后面24为的排列中, 取整数的前8位, 看是不是1, 然后去掉后面的16位, 获取前八位的值
>>> b3 = (n & 0xff00) >> 8
>>> b4 = n & 0xff
>>> bs = bytes([b1, b2, b3, b4]) # 数值的高位放在存储器地址的低位,是大端
>>> bs

"""

import struct

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# 以上相当于
ret = struct.pack(">I", n) # '>'表示big-endian, 'I'表示4字节无符号整数
print(ret)

# unpack可以理解为逆运算
reverse_n = struct.unpack(">I", ret) # 返回一个元组
print(reverse_n)

ret = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80') # H: 2字节无符号整数, 将字节流转解析成换成两个数
print(ret)

# 跳过填充位
record = b'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = struct.unpack(">10sHHb", record) # 无论是用大端还是小端,结果都是一样的...
print((name, serialnum, school, gradelevel)) # name是bytes

# 顺序不同, size不同
print(struct.calcsize('ci'))
print(struct.calcsize('ic'))
# The ordering of format characters may have an impact on size since the padding needed to satisfy alignment requirements is different

"""
      struct header

      {

          unsigned short  usType;

          char[4]               acTag;

          unsigned int      uiVersion;

          unsigned int      uiLength;

      };
"""
# 如果知道被封装的结构体的形式是这样的, 可以这么解析
string = struct.pack('H4sII', 0x04, b'aaaa', 0x01, 0x0e) # 网页上是'B4sII'
print(string)
print(struct.unpack('H4sII', string))

#-------------------------------------------------------------------------#
stu = struct.Struct(">I4sf") # 类似re.compile
print(dir(stu))
