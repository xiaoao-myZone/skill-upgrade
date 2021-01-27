from threading import Thread, Lock
import traceback
lock = Lock()

def lock_thread():
    def _wrapper(func):
        def __wrapper(lock, *args, **kwargs):
            lock.acquire()
            try:
                ret = func(lock, *args, **kwargs)
                lock.release()
                return ret
            except:
                traceback.print_exc()
                lock.release()
        return __wrapper
    return _wrapper

@lock_thread()
def func(lock, num):
    # lock.acquire()
    # try:
    if num==3:
        raise Exception("error")
    print("num %s say hi~" % num)
    # finally:
    #     lock.release()

for i in range(1,10):
    thread = Thread(target=func, args=(lock, i))
    thread.start()