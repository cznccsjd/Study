#coding:utf-8
"""
threading模块的对象Lock、RLock、Condition、Semaphore和BoundedSemaphore都包含上下文管理器，
也就是说，他们都可以使用with语句。当使用with时，可以进一步简化loop()循环。
代码如下所示：
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
    with lock:
        remaining.add(my_name)      #使用集合记录正在运行的线程
        print('[%s] Started %s'%(ctime(), my_name))

    sleep(nsec)     #2、每个进程随机睡眠2~4秒
    with lock:
        remaining.remove(my_name)
        print('[%s] Completed %s (%d secs)' %(ctime(), my_name, nsec))
        print('    (remaining:%s)'%(remaining or 'None'))

def _main():
    for pause in loops:     #1、随机创建3~6个进程
        print('pause的值：%s' %pause)
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()