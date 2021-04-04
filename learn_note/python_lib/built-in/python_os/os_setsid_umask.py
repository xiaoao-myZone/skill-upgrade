#-*- coding: utf-8 -*-
"""referrence: https://blog.csdn.net/sweetfather/article/details/79457261"""
import os

os.setsid #用于子线程中，更改子线程的parent pid，也即将当前子线程移出主进程
os.umask #作用在进程操作文件时，将输入umask的参数取反，然后与当前操作权限相与，入os.umask(0)，进程得到的权限为0777