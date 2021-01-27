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

            print("[Task_Planner] reort shelf, receiving shelf info: %s" %response)
            #you can report shelf info to WCS
            self.status = WS.batch
            response = yield "shelf bind success"


            print("[Task_Planner] reort tote, receiving tote info: %s" %response)
            #you can report tote info to WCS 
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
    while True:

        ans = raw_input("\nenter:")
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






