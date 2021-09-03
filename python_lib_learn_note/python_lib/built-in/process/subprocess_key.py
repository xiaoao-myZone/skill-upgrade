import subprocess

proc = subprocess.Popen(['sleep', '1'])
proc.communicate()
# Interact with process: Send data to stdin and close it.
# Read data from stdout and stderr, until end-of-file is reached.
# Wait for process to terminate.

# shell参数会为进程再创建一个terminal， 并且返回的是这个terminal的pid， 杀死这个terminal，里面的子线程不会被杀死
"""
reference:
1. https://blog.csdn.net/besmarterbestronger/article/details/94738845
2. https://blog.csdn.net/besmarterbestronger/article/details/94738845
"""
