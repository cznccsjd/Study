#coding:utf-8
"""
线程优先级队列（ Queue）
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:

Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""

import queue
import threading
import time

exit_flag = 0

class myThread(threading.Thread):
    def __init__(self, thread_id, name, q, num):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q
        self.num = num

    def run(self):
        print("开启线程：" + self.name)
        print("执行process_data之前，num=", self.num)
        process_data(self.name, self.q, self.num)
        print("退出线程：" + self.name)
        print("退出线程后，num=", num)

def process_data(thread_name, q, num):
    print("进入Process_data的时间：", time.monotonic_ns())
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print("%s processing %s" %(thread_name, data))
            print('此时num=', num)
            num +=1
        else:
            print("%s 队列为空，释放锁了" % thread_name)
            print("此时在else中，num=", num)
            num += 1
            queue_lock.release()
        time.sleep(1)


num = 1
queue_lock = threading.Lock()
work_queue = queue.Queue(10)
threads = []
thread_id = 1

thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["One", "Two", "Three", "Four", "five"]

# 创建新进程
for t_name in thread_list:
    thread = myThread(thread_id, t_name, work_queue, num)
    thread.start()
    threads.append(thread)
    thread_id += 1
    print("这里的num也+1了")
    num  += 1

# 填充队列
queue_lock.acquire()
for n_list in name_list:
    print("进入填充队列的时间：", time.monotonic_ns())
    print("开始填充%s，此时num=%d" %(n_list, num))
    num += 1
    work_queue.put(n_list)
    print("%s, 填充完成,此时num=%d" %(n_list, num))
    num +=1
queue_lock.release()

# 等待队列清空
while not work_queue.empty():
    pass

# 通知队列是时候退出
exit_flag = 1

# 等待所有队列完成
for t in threads:
    print("等待队列完成时的时间：", time.monotonic_ns())
    print("%s开启等待，此时num=%d" %(t, num))
    num += 1
    t.join()
    print("%s 的join方法执行完成，此时num=%d" % (t, num))
    num+=1
    print("队列确认完成时的时间：", time.monotonic_ns())
print("退出主线程")