#coding:utf-8
"""
该生产者 - 消费者问题的实现使用了 Queue 对象，以及随机生产（消费）的商品的数量。生产者和消费者独立且并
发地执行线程。
"""

from random import randint
from time import sleep
from queue import Queue
from process_thread_asynchrony.study_with_python3_threading_202107.threading_7_Thread import MyThread

def writeQ(queue):
    print('producing object for Q...')
    print(f'put之前，queue的size是{queue.qsize()}')
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def readQ(queue):
    print(f'get之前的queue的size是{queue.qsize()}')
    queue.get(1)
    print('consumed object form Q...size now', queue.qsize())

def writer(queue, loops):
    print(f'wirter传入的queue值是{queue}')
    for i in range(loops):
        print(f'第{i + 1}次调用writeQ()')
        writeQ(queue)
        nsec = randint(1, 3)
        print(f'第{i + 1}次调用writeQ时，sleep了{nsec}秒')
        sleep(nsec)

def reader(queue, loops):
    print(f'reader传入的queue的值是{queue}')
    for i in range(loops):
        print(f'第{i + 1}次调用readQ方法')
        readQ(queue)
        nsec = randint(2, 5)
        print(f'第{i + 1}次调用readQ时，sleep了{nsec}秒')
        sleep(nsec)

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    print(f'本次nloops的值：{nloops}')
    q = Queue(32)
    print(f'main中生成的q是{q}')

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

if __name__ == '__main__':
    main()