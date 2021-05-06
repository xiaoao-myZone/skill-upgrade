import os
read_pipe, write_pipe = os.pipe() # create pipe from 3
os.close(read_pipe) # close pipe
os.close(write_pipe) # close pipe

"""
referrence https://blog.csdn.net/qq_35037977/article/details/77751119
"""
os.execve #os.exec**
os.spawnv
os.fork
os.dup2
os.pipe

pid = os.fork()
print("pid: %d" % pid)
if pid !=0:
    print("this is parent pid:%d" % pid)
else:
    print()
    print("this is child pid: %d" % os.getpid())