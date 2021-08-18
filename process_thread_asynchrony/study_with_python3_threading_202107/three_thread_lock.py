#coding:utf-8
"""
引入锁
thread模块函数
allocate_lock()    分配lockType锁对象
exit()    给线程退出指令

LockType锁对象的方法
acquire(wait=None)    尝试获取锁对象
locked()    如果获取了锁对象则返回True，否则，返回False
release()    释放锁
"""

import _thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
    print("start loop%d at: %s" %(nloop, ctime()))
    sleep(nsec)
    print("loop%d done at: %s" %(nloop, ctime()))
    lock.release()

def main():
    print("starting at:", ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print("all DONE at:", ctime())

if __name__ == '__main__':
    main()