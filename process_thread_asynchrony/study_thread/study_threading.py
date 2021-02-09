#coding:utf-8
"""
多线程学习
"""

import threading
import time

'''
print('返回当前的线程变量：', threading.current_thread())
print('返回一个包含正在运行得线程list：', threading.enumerate())
print("返回正在运行得线程数量:", threading.activeCount())
# 设置threading全局超时时间
threading.TIMEOUT_MAX = 10
'''

####################
# Thread类
####################
'''
print('run()，用以表示线程活动的方法：threading.Thread().run()')
print('strt()，启动线程活动：')
print('join([time])，等待至线程中止。')
print('isAlive()，返回线程是否活动。')
print('getName()，返回线程名。')
print('setName()，设置线程名。')
'''

########################
# 使用threading模块创建线程
########################
'''
exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        self.print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新进程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
'''

###################
# 线程同步
###################
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")