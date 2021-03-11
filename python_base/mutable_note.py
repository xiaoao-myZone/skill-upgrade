import time
from threading import Thread

class Test(object):
    connect_list = []
    def add(self, addr):
        self.connect_list.append(addr)

class ModifiedTest(Test):
    max_len = 10
    def add(self, addr):
        self.check_length()
        self.connect_list.append(addr)
    def check_length(self):
        if len(self.connect_list) >= self.max_len:
            # while self.connect_list:
            #     self.connect_list.pop()
            self.connect_list = []


test = ModifiedTest()
def check_conn_list(conn_list):
    while True:
        if "127.0.0.1" in conn_list:
            print("find connection from local")
        time.sleep(0.1)
thread = Thread(target=check_conn_list, args=(test.connect_list,))
thread.daemon = True
thread.start()
for i in range(10):
    test.add("192.168.1.1")
test.add("127.0.0.1")
time.sleep(5)