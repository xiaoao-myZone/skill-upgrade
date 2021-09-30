import numpy as np

# 初始化narray
normal = np.array([1, 2, 3, 4])
print(f"{normal=}")
zero = np.zeros(3, dtype="int")
print(f"{zero=}")
one = np.ones(3, dtype="int")
print(f"{one=}")
full = np.full(3, 100, dtype="int")
print(f"{full=}")
# 以上第一个参数都可以变为数组， 表示多维


# 均分
arange = np.arange(1, 10, 3)  # 跨步
print(f"{arange=}")
liner = np.linspace(1, 15, 3)  # 等分
print(f"{liner=}")

# 随机
ran1 = np.random.random((5, 3))  # 没有参数返回浮点， 有一个整型参数返回一维数组， 有一个数组输入， 返回对应维数
print(f"{ran1=}")  # 0~1
ran2 = np.random.normal(0, 1, (4, 6))  # 分别是期望， 标准差，与维度
# TODO 一个随机分布获得的数值，如何通过一个函数转化为， 其输出变为正态分布
print(f"{ran2=}")  # 0~1
ran3 = np.random.uniform(7, 8, (3, 3))
print(f"{ran3=}")  # 7~8


# dtype的种类
np.int0, np.intc, np.int8, np.int16, np.int32, np.int64
# int0=int64  intc与C语言中的int一致
np.float32, np.float64, np.longdouble
np.complex64
np.uint


# 切片
# 对单维的操作与python中list的做法一致, start:end:step
print([1, 2, 3, 4, 5][::-1])  # 注意当step为-1时， 如果不指名前两个，则认为是end: start
print(f"{ran1[:2, :3]=}")


"""
特别注意：
    1. 当给narray中的整型元素赋值的时候， 如果是浮点型， 会自动进行类型转换， 且没有提示
    2. 当使用切片的时候， 返回的结果是引用，而不是拷贝，所以子序列改动会影响整个序列
"""
