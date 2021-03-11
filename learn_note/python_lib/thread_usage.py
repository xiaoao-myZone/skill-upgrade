import time
from threading import Thread, Lock
def func(lock):
    with lock:
        time.sleep(1)
        print("hi")

lock = Lock()
for i in range(10):
    Thread(target=func, args=(lock, )).start()