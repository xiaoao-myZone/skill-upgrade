#-*- coding: utf-8 -*-
from queue import LifoQueue
def to_binary(num, stack=None):
    if not isinstance(num, int) or num < 0:
        return

    if stack is None:
        stack = LifoQueue()
    if num == 0:
        s = []
        while not stack.empty():
            bit = stack.get_nowait()
            s.append(str(bit))
        print("".join(s))
        return
    bit = num % 2
    stack.put_nowait(bit)
    num = num // 2
    to_binary(num, stack)




a = 40
b = 45
c=a&b
d = a|b
e = a^b
f = ~a
to_binary(a)
to_binary(b)
to_binary(c)
to_binary(d)
to_binary(e)
# to_binary(f)
print(f)

# 移位
print("-------------------")
a = 1024
to_binary(a)
b = a>>2
print(b)
to_binary(b)