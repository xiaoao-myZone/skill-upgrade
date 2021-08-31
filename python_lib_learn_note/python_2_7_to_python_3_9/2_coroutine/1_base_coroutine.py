
import inspect


def fibo():
    yield 1
    a, b = 0, 1
    for _ in range(10):
        c = a + b
        yield c
        a, b = b, c


f = fibo()
print(inspect.getgeneratorstate(f))  # inspect.GEN_CREATED
print(next(f))
print(inspect.getgeneratorstate(f))  # inspect.GEN_SUSPENDED
for _ in range(11):
    try:
        print(next(f))
    except StopIteration:
        print(inspect.getgeneratorstate(f))  # inspect.GEN_CLOSED
        # 除非抛出这个异常， 不然得到的状态一直是GEN_SUSPENDED
f.close()  # f可以在任意时候close
try:
    f.throw(Exception("test"))  # 如果迭代器中没有捕获这个异常， 将会抛回给f.throw自己
    # 如果捕获了， f.throw将会获得yield中的值
except Exception as e:
    print(e)
# 另外还有一个GEN_RUNNING, 可以顾名思义
# 参考: https://blog.csdn.net/miuric/article/details/84859785
