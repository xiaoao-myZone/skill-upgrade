"""typing 在python3.5引入"""

from typing import List, Dict


# 注意， Dict的声明不是Dict[int: str]
def func(msg: Dict[int, str]) -> List[str]:
    return list(msg.values())


if __name__ == "__main__":
    msg = {
        1: "我",
        2: "不叫",
        3: "喂!"
    }
    ret = func(msg)
    print(ret)
