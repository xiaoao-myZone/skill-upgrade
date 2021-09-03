#!/usr/bin/env python
import time
from enum import Enum
WS = Enum("status", "start shelf batch working")


class Task_Planner():
    def __init__(self):
        self.status = WS.start
    # main workflow

    def run(self):
        print("[Task_Planner] run ...")
        while True:

            print("[Task_Planner] start")
            # you can prepare to start
            self.status = WS.shelf
            response = yield "start success"

            print("[Task_Planner] reort shelf, \
                receiving shelf info: %s" % response)
            # you can report shelf info to WCS
            self.status = WS.batch
            response = yield "shelf bind success"

            print("[Task_Planner] reort tote, \
                receiving tote info: %s" % response)
            # you can report tote info to WCS
            self.status = WS.working
            # start rebinning
            print("picking.....")
            time.sleep(0.5)
            print("updating.....")
            time.sleep(0.5)
            self.status = WS.start
            response = yield "gain batch success"


# they can be called by http
def start_cmd(task_planner, run_iter):
    if task_planner.status == WS.start:
        r = run_iter.send(None)
        print("[start_cmd] %s" % r)
    else:
        print("failed")


def bind_shelf_cmd(task_planner, run_iter):
    if task_planner.status == WS.shelf:
        info = "shelf id: 2"
        r = run_iter.send(info)
        print("[bind_shelf_cmd] %s" % r)
    else:
        print("failed")


def send_batch_cmd(task_planner, run_iter):
    if task_planner.status == WS.batch:
        info = "batch id: 25488"
        r = run_iter.send(info)
        print("[send_batch_cmd] %s" % r)
    else:
        print("failed")


if __name__ == "__main__":
    task_planner = Task_Planner()
    run_iter = task_planner.run()
    print("###enter 1 to start")
    print("###enter 2 to send shelf")
    print("###enter 3 to send batch")
    # m = run_iter.send(None)
    # send第一次一定要发送一个None， 不然会出现TypeError
    while True:

        ans = input("\nenter:")
        if ans.isalnum():
            ans = int(ans)
        else:
            print("wrong command")
        if ans == 1:
            start_cmd(task_planner, run_iter)
        elif ans == 2:
            bind_shelf_cmd(task_planner, run_iter)
        elif ans == 3:
            send_batch_cmd(task_planner, run_iter)
        else:
            print("wrong command")

# 1. yield的send相当于互换了一次值， yield把其后面的值作为了send的返回值， send把参数给了yield的返回值
# 2. 根据send需要先发送None的特点， 我们大概可以知道， 这个交换其实是有一个错配的过程， 并且是，
#    被卡住的yield先获得send发来的参数作为返回值， 并且返回了下一个yield后面的值给send当做返回值， 同时卡在
#    这个yield上。
# 3. 这也意味着， 第一次的send注定会被丢失， 抛出异常， 我猜是因为这个机制确实比较费解， 怕开发者没有理解这个细节，
#    而在实际应用中犯错， 所以给了带值的第一个send一个异常， 作为警告。
# 4. 迭代器与生成器有何区别? 生成器就是有一个或者多个yield的函数返回的对象， 迭代器就是有__iter__方法的对象
#    ，生成器一定有__iter__方法， 所以生成器一定是迭代器， 反之不一定。
