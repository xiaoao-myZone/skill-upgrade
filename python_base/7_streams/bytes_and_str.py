# str --> bytes
# bytes --> str
# bytes(\x) --> int
# str --> int
# with open("/dev/random", "rb") as f:
#     seed = f.read(100)
#     print(seed)

# print(bytes(map(ord, '\x01\x02\x31\x32')).decode())
import struct


UINT32_MAX = 0xffffffff
_random_source = open("/dev/random", "rb")


def random_bytes(len):
    return _random_source.read(len)


def unpack_uint32(bytes):
    tup = struct.unpack("I", bytes)
    # 输出的是一个长度为1的元祖， 元素大小估计为2<<32 - 1 的无符号整数
    return tup[0]


def randint(low, high):
    """
    Return a random integer in the range [low, high], including
    both endpoints.
    """
    # n = (high - low) + 1
    # assert n >= 1
    # scale_factor = n / float(UINT32_MAX + 1)
    # random_uint32 = unpack_uint32(random_bytes(4))
    # # 我觉得求余可能更简单并且直观
    # result = int(scale_factor * random_uint32) + low
    # return result
    n = (high - low) + 1
    assert n >= 1
    random_uint32 = unpack_uint32(random_bytes(4))
    result = random_uint32 % n + 1
    return result


def randint_gen(low, high, count):
    """
    Generator that yields random integers in the range [low, high],
    including both endpoints.
    """
    n = (high - low) + 1
    assert n >= 1
    scale_factor = n / float(UINT32_MAX + 1)
    for _ in range(count):
        random_uint32 = unpack_uint32(random_bytes(4))
        result = int(scale_factor * random_uint32) + low
        yield result


if __name__ == "__main__":
    # roll 3 dice individually with randint()
    count_a = {k: 0 for k in range(1, 7)}
    count_b = {k: 0 for k in range(1, 7)}
    times = 100000
    for _ in range(times):
        for i in [randint(1, 6) for _ in range(3)]:
            count_a[i] += 1

        # roll 3 dice more efficiently with randint_gen()
        for i in randint_gen(1, 6, 3):
            count_b[i] += 1
    for i in count_a:
        count_a[i] /= float(times)
    for i in count_b:
        count_b[i] /= float(times)
    print(f'{count_a=}')
    print(f'{count_b=}')
"""
Referrence:
1. python常用的十进制、16进制、字符串、字节串之间的转换
   https://blog.csdn.net/woxiaozhi/article/details/58603865
2. 如何使用Python从/dev/random中获取数字？ https://www.cnpython.com/qa/74294
"""
