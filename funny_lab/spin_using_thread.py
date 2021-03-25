import threading
import itertools
import time
import sys


class Signal:
    go = True

def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + " " + msg
        write(status)
        flush()
        write('\x08' * len(status)) # \x08一定是回退符号
        time.sleep(0.1)
        if not signal.go:
            break
    write(' '*len(status) + '\x08' * len(status))

def slow_function():
    time.sleep(5)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking', signal))
    spinner.daemon = True
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print("Answer:", result)

if __name__ == "__main__":
    main()


"""
'\x08'写入输出流可以让光标回退(不会删除), 接着写入会覆盖光标后的字符
"""