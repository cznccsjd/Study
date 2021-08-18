#coding:utf-8
"""
与eleven_threading_Thread_lock_adv.py相比，没有添加锁，可以会有输出部分混乱的问题；
"""

from atexit import register
from random import randrange
from threading import Thread, current_thread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
    my_name = current_thread().name
    print("这里获取了my_name：%s " % my_name)
    remaining.add(my_name)
    print('[%s] Started %s'%(ctime(), my_name))
    sleep(nsec)
    remaining.remove(my_name)
    print('[%s] Completed %s (%d secs)' % (ctime(), my_name, nsec))
    print('    (remaining: %s)' % (remaining or 'NONE'))

def _main():
    for pause in loops:
        print(pause)
        Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()