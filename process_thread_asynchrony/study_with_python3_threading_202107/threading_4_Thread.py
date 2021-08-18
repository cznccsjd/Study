#coding:utf-8
"""
Thread对象数据属性：
start()    开始执行该线程
join(timeout=None)  直至启动的线程终止之前一直挂起；除非给出了timeout(秒)，否则会一直阻塞
PS: join()被称为自旋锁，比three_thread_lock.py中的等待锁释放的无限循环更加清晰

Thread对象方法：
__init__(group=None,target=None,name=None,args=(),kwargs={},verbose=None,daemon=None)
实例化一个线程对象，需要有一个可调用的target，以及其参数args或kwargs。还可以传递name或group参数，不过后者还未实现。
而daemon的值将会设定thread.daemon属性/标志

使用Thread类，可以有很多方法来创建线程：
第一种：创建Thread的实例，传给它一个函数
第二种：创建Thread的实例，传给它一个可调用的类实例
第三种：派生Thread的子类，并创建子类的实例
"""
import threading
from time import sleep, ctime

loops = [4, 2]
def loop(nloop, nsec):
    print("start loop%d at: %s" %(nloop, ctime()))
    sleep(nsec)
    print("loop%d done at: %s" %(nloop, ctime()))

def main():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 创建Thread的实例，传给它一个函数
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    # start threads
    for i in nloops:
        threads[i].start()

    # wait for all
    for i in nloops:
        threads[i].join()    #threads to finish

    print("all DONE at:", ctime())

if __name__ == '__main__':
    main()