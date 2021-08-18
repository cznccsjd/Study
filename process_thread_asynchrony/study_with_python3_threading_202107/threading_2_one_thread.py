#coding:utf-8
"""
调用_thread.start_new_thread(),初步实现多进程
thread模块函数
start_new_thread(function,args,kwargs=None) 派生一个新线程，使用给定的args和可选的kwargs来执行function
"""

import _thread
from time import sleep, ctime

def loop0():
    print("start loop 0 at:", ctime())
    sleep(4)
    print("loop 0 done at:", ctime())

def loop1():
    print("start loop 1 at:", ctime())
    sleep(2)
    print("loop 1 done at:", ctime())

def main():
    print("starting at:", ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print("all DONE at:", ctime())

if __name__ == '__main__':
    main()