import sys
import time
from multiprocessing import Process
from threading import Thread

def func(name):
    while True:
        print("%s say hi~" % name)
        time.sleep(1)

P = Process(target=func, args=("test_1",))
T = Thread(target=func, args=("test_2",))
P.daemon = False
T.daemon = True

if __name__ == "__main__":
    P.start()
    print(P.pid)
    print(P.sentinel)
    # T.start()
    # print(T.ident)
    time.sleep(4)
    P.terminate()
    time.sleep(1)
    P.start()

"""
Conclusion:
    It's easy to kill Process at any time with method terminate
    It's not immediate to kill a thread
"""
    

