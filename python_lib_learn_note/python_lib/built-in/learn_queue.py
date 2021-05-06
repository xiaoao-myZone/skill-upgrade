
# import eventlet
# eventlet.monkey_patch()
# from gevent import monkey;monkey.patch_all()

from threading import Thread
from random import randint
import time
import logging
from Queue import Queue
logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger("Queue")
q = Queue(20)
# q.mutex
def recv(q):
    for _ in range(20):
        time.sleep(randint(2,9)*0.1)
        q.put("apple")
        logger.info("get an apple")


def eat_apple(q,name):
    logger.info("thread-%s is finding fruit..." % name)
    time.sleep(randint(2,10)*0.1)
    logger.info("thread-%s ready to eat apple..." % name)
    #q.join()
    res = q.get()
    # if name == 4:
    #     raise Exception("some wrong")
    logger.info("I eat a/an %s" % res)
    #q.task_done() # to release q.join()
    logger.info("thread-%s end" % name)

recv_thread = Thread(target=recv, args=(q,))
recv_thread.start()

s_thread = None
for i in range(20):
    name = i+1
    thread = Thread(target=eat_apple, args=(q,name), name="thread-%s" %name)
    if name == 4:
        s_thread = thread
    thread.start()
time.sleep(0.4)
Thread._Thread__stop(s_thread)

q.join()



