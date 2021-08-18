#/usr/bin/python3
#coding:utf-8
"""
使用 threading 模块创建线程
我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法
"""

import threading
import time

exit_flag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程:" + self.name)
        print(time.ctime(time.time()))
        print_time(self.name, self.counter, 5)

def print_time(threadName, delay, counter):
    while counter:
        if exit_flag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" %(threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join(1)
# print('thread1,第一次检测alive:' , thread1.isAlive())
# print('thread2,第一次检测alive:',thread2.isAlive())
thread2.join(1)
# print('thread1,第二次检测alive：',thread1.isAlive())
# print('thread2，第二次检测alive:',thread2.isAlive())
print("退出主线程")