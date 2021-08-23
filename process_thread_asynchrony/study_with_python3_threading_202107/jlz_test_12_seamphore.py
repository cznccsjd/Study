#coding:utf-8

#coding:utf-8
"""
结合threading_13_semaphore.py，自建一个class，继承BoundedSeamphore，调用self.value，查看实际的值
"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

class MyTest(BoundedSemaphore):
    '''
    哈哈哈哈哈，不会了，需要怎么才能调用到内嵌的self._value
    '''
    def __init__(self):
        self.is_value = self.value

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