#-*- coding: utf-8 -*-
"""referrence: https://blog.csdn.net/zhupenghui176/article/details/109097737"""
import os
import time
import signal
print("main main pid")
print(os.getppid())
print("main pid:%d" % os.getpid())
def fork(cmd, times=3):
    r, w = os.pipe()
    pid = os.fork()
    if pid:
        os.close(w)
        return pid, r
    else:
        os.close(r)
        os.close(0)
        os.dup2(w, 1)
        os.dup2(w, 2)
        cmd = cmd.split()
        print("child pid: %d" % os.getpid())
        print("the parent pid of child: %d" % os.getppid())
        for _ in range(times):
            time.sleep(0.1)
        os._exit(0) # 如果不退出子进程，子进程会继续执行pid, r = fork("ping 127.0.0.1")，从而报错
        #raise Exception("afsaf")
        #os.execlp(cmd[0], cmd[0], *cmd[1:])

res = []
res.append(fork("ping 127.0.0.1", 5))
res.append(fork("ping 127.0.0.1"))


# 如果没有子进程会报错， 有子进程但是没有停止的，返回(0, 0)，有停止的子进程(pid, 256) WNOHANG(wait no hung) 其值为1
# option=os.WNOHANG, 如果有两个子进程结束了会如何? 答：会返回pid较小的那一个
# option=0, 如果有两个子进程结束了会如何? 答：会返回pid较小的那一个

# waitpid返回的第二个参数表示的是进程结束的方式 o: os._exit(0)正常退出， 256：os._exit(1)异常退出,对应python err
# wait_res = os.waitpid(-1, os.WNOHANG)
# print(wait_res)

# time.sleep(1) #wait for all subprocess stop
for _ in res:
    ret = os.waitpid(-1, os.WNOHANG)
    print("detect subprocess over%s" % str(ret))
try:
    ret = os.waitpid(-1, 0)
    print(ret)
except:
    print("无正在运行的子程序")
for i in res:
    print(os.read(i[1], 1024))
# if not res[0]:
#     os.kill(pid, signal.SIGINT)