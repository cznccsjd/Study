#coding:utf-8
"""
验证下同时启动多个线程，和一个线程里面添加for循环的场景
"""

from atexit import register
from threading import Thread
from time import sleep, ctime
from random import randint

def test(n,nsec):
    print(f'第{n+1}次进入test方法，当前时间:', ctime())
    print(f'第{n+1}次准备sleep{nsec}秒；')
    sleep(nsec)
    print(f'第{n+1}次sleep完了，这时候时间为：', ctime())

def test2():
    for i in range(3):
        n = randint(1, 5)
        test(i,n)

def _main():
    '''
    启动多个线程，全部线程在同一时间内启动
    '''
    print('整个程序开始运行:', ctime())
    for i in range(3):
        n = randint(1, 5)
        Thread(target=test, args=(i,n,)).start()

def _main2():
    '''
    实际上只启动了一个线程，然后有个for循环，来控制test2()的启动时间
    '''
    print('整个程序开始运行:', ctime())
    Thread(target=test2, args=()).start()


@register
def _atexit():
    print('ALL DONE:', ctime())

if __name__ == '__main__':
    # _main()
    _main2()