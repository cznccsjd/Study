#coding:utf-8

"""
创建Thread的实例，传给它一个可调用的类实例
在创建线程时，与传入函数相似的一个方法是传入一个可调用的类的实例，用于线程执行。
这种方法更加接近面向对象的多线程编程。这种可调用的类包含一个执行环境，比起一个函数或者从一组函数中选择而言，
有更好的灵活性。现在你有了一个类对象，而不仅仅是单个函数或者一个函数列表/元组。
"""

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
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
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all DONE at:", ctime())

if __name__ == '__main__':
    main()