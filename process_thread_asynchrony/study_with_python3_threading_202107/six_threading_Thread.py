#coding:utf-8
"""
派生Thread的子类，并创建子类的实例
与five_threading_Thread.py相比，不同点：
1、MyThread子类的构造函数必须先调用其基类的构造函数(threading.Thread.__init__(self))
2、之前的特殊方法_call_()在这个子类中必须要写为run()
"""
import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print("start loop%d at: %s" %(nloop, ctime()))
    sleep(nsec)
    print("loop%d done at: %s" %(nloop, ctime()))

def main():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all DONE at:", ctime())

if __name__ == '__main__':
    main()