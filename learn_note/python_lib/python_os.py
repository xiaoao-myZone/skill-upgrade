import os
read_pipe, write_pipe = os.pipe() # create pipe from 3
os.close(read_pipe) # close pipe
os.close(write_pipe) # close pipe
os.execve
os.spawnv