from typing import Any


class Local:
    # storage = {}
    def __init__(self) -> None:
        # 由于__setattr__已经被定了， 如果用self.storage={}，会出现max recursion depth error
        object.__setattr__(self, "storage", {})

    def __setattr__(self, name: str, value: Any) -> None:
        print(f"store {name}: {value}")
        self.storage[name] = value

    def __getattr__(self, name: str) -> Any:
        if name in self.storage:
            print(f"get {name}")
            return self.storage[name]
        else:
            raise AttributeError


ll = Local()
ll.a = 3
print(ll.a)

# 本质上来说， 一般的类， 其实是通过__dict__来代替 上面例子中的__storage__

import enum
class Enum(object):
    @classmethod
    def __setattr__(cls, name, value):
        print(f'{name}={value}')


class Student(Enum):
    name = "Paul"


print(f'{Student.name=}')