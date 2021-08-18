#coding:utf-8
"""
锁示例
锁有两种状态：锁定和未锁定，支持两个函数：获得锁和释放锁
当多线程争夺锁时，允许第一个获得锁的线程进入临界区（eg：I/O 和访问相同的数据结构都属于临界区），并执行代码。所有之后到达
的线程将被阻塞，直到第一个线程执行结束，退出临界区，并释放锁。此时，其他等待的线
程可以获得锁并进入临界区。不过请记住，那些被阻塞的线程是没有顺序的（即不是先到先
执行），胜出线程的选择是不确定的，而且还会根据 Python 实现的不同而有所区别。

让我们来看看为什么锁是必需的。ten_threading_Thread_lock.py 应用派生了随机数量的线程，当每个线程
执行结束时它会进行输出。
"""
from atexit import register
from random import randrange
from threading import Thread, current_thread, Lock
from time import sleep, ctime

class CleanOutputSet(set):
    # 其实是设置了个集合，存放线程名
    def __str__(self):
        return ','.join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
    my_name = current_thread().name
    print("这里获取了my_name：%s "%my_name)
    lock.acquire()
    remaining.add(my_name)      #使用集合记录正在运行的线程
    print('[%s] Started %s'%(ctime(), my_name))
    lock.release()
    sleep(nsec)     #2、每个进程随机睡眠2~4秒
    lock.acquire()
    remaining.remove(my_name)
    print('[%s] Completed %s (%d secs)' %(ctime(), my_name, nsec))
    print('    (remaining:%s)'%(remaining or 'None'))
    lock.release()

def _main():
    for pause in loops:     #1、随机创建3~6个进程
        print('pause的值：%s' %pause)
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()