#-*- coding: utf-8 -*-
"""
Referrence: https://www.cnblogs.com/kuliuheng/p/4946176.html
"""
import logging

"""
Raw log
"""
# print("--------------------*--------------------")
# logging.debug("debug") # no output
# logging.info("info") # no output
# logging.warn("warning") # WARNING:root:warning
# logging.error("error") # ERROR:root:error

"""
Conclusion:
    1. default log level is warn
    2. default log name is root
"""

print("--------------------*--------------------")
"""
Global config (I guess)
"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S %Y-%m-%d",
    filename="xyz.log",
    filemode="w"
    
    )
""""""
logging.debug("debug") 
logging.info("info") 
logging.warn("warning") 
logging.error("error") 

"""
Conclusion:
    1. basicConfig must be used before debug, info, warn error and etc method, or it will not have effect
    2. if only use one log file in the process, you can use filename
    3. stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略 %(levelno)s: 打印日志级别的数值
    4.  %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d: 打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d: 打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息
"""

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)-5s: %(levelname)-8s %(message)s")
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.info("a lo ha")


"""
日志轮替
"""
from logging.handlers import RotatingFileHandler
Rt_handler = RotatingFileHandler("mm.log", maxBytes=1024*2, backupCount=3)
Rt_handler.setLevel(logging.DEBUG)
Rt_handler.setFormatter(formatter)
logging.getLogger('').addHandler(Rt_handler)
for i in range(20):
    logging.info("世上无难事没只怕有心人")

"""
Conclusion:
    1. 备份文件后缀为log.1~maxNum
    2. sample.log永远为最新的，其次是1,2,3，...

"""


