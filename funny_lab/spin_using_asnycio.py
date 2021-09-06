import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + " " + msg
        write(status)
        flush()
        write('\x08' * len(status))  # \x08一定是回退符号
        try:
            yield from asyncio.sleep(.1)  # 也就是在协程中能暂停的只有asyncio.sleep
        except asyncio.CancelledError:
            break
    write(' '*len(status) + '\x08' * len(status))  # 清空


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42


# @asyncio.coroutine
# def supervisor():
#     spinner = asyncio.async(spin('thinking'))  # 排定spin协程的运行时间
#     print("spinner object:", spinner)
#     result = yield from slow_function()
#     spinner.cancel()
#     return result


def main():
    loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(supervisor())
    result = loop.run_until_complete(spin('thinking'))
    loop.close()
    print("Answer:", result)


if __name__ == "__main__":
    main()

"""
asyncio.coroutine 和 yield from 配套使用
"""
