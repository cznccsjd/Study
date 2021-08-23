#coding:utf-8
"""
信号量示例
如前所述，锁非常易于理解和实现，也很容易决定何时需要它们。然而，如果情况更加
复杂，你可能需要一个更强大的同步原语来代替锁。对于拥有有限资源的应用来说，使用信
号量可能是个不错的决定。
信号量是最古老的同步原语之一。它是一个计数器，当资源消耗时递减，当资源释放
时递增。你可以认为信号量代表它们的资源可用或不可用。消耗资源使计数器递减的操作
习惯上称为P() （来源于荷兰单词probeer/proberen），也称为wait、try、acquire、pend或procure。
相对地，当一个线程对一个资源完成操作时，该资源需要返回资源池中。这个操作一般称
为 V()（来源于荷兰单词 verhogen/verhoog），也称为 signal、increment、release、post、vacate。
Python 简化了所有的命名，使用和锁的函数/方法一样的名字：acquire 和 release。信号量比
锁更加灵活，因为可以有多个线程，每个线程拥有有限资源的一个实例。
在下面的例子中，我们将模拟一个简化的糖果机。这个特制的机器只有 5 个可用的槽来
保持库存（糖果）。如果所有的槽都满了，糖果就不能再加到这个机器中了；相似地，如果每
个槽都空了，想要购买的消费者就无法买到糖果了。我们可以使用信号量来跟踪这些有限的
资源（糖果槽）。
"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill(times):
    print(f'第{times + 1}次，启动refill行为：', ctime())
    lock.acquire()
    print('Refilling candy...')

    try:
        aa = candytray.release()
        print(f'第{times + 1}次refil后，BoundSeamphore的release结果是：{aa}，当前时间:{ctime()}')
    except ValueError:
        print('full, skipping')
    else:
        print('refil,OK')
    lock.release()

def buy(times):     #time参数时自己额外添加的，只是想配合打印下时间
    print(f'第{times+1}次，启动buy行为：', ctime())
    lock.acquire()
    print('Buying candy...')
    aa = candytray.acquire(False)
    print(f'第{times+1}次买完后，BoundSeamphore的acquire结果是：{aa}，当前时间：{ctime()}')

    if aa:
        print('buy,OK')
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    print(f'打算refill{loops}次')
    for i in range(loops):
        refill(i)
        s_time = randrange(3)
        print(f'第{i + 1}次refill时，被强制sleep了{s_time}秒')
        sleep(s_time)

def consumer(loops):
    print(f'这次打算买{loops}次。')
    for i in range(loops):
        buy(i)
        s_time = randrange(3)
        print(f'第{i+1}次buy时，还被强制sleep了{s_time}秒')
        sleep(s_time)

def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print(f'nloops={nloops}')
    print(f'THE CANDY MACHINE (full with {MAX} bars)!')
    # buyer
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    # vndr
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()