"""
进程: 进程是正在执行的程序的实例

内核会为进程记录: 
1. 进程ID  os.getpid()
2. 用户ID  os.getuid() # import pwd; pwd.getpwuid(os.getuid) #可获取用户的详细信息
3. 组ID    os.getgid()
4. 终止状态  #终止的时候才有  os.waitpid(-1/pid, 0/1)
5. 父进程ID os.getppid()

os.fork() 内核通过对父进程的复制来创建子进程
os.execve()在子进程中删掉当前的文本段, 数据段, 栈段以及堆段, 并根据输入参数创建新段来替换


终止进程:
1. _exit()

"""
import os
print(os.getppid()) # TODO 如果是开机自启, parent id为多少?
# os.fork()
# if os.getpid()==-1:
#     os._exit(0)
# os.waitpid()