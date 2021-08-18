#coding:utf-8
"""
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。

那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。

锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。

经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
"""
import threading, time

lists = [3, 1, 1, 2]
class myThread(threading.Thread):
    def __init__(self, name, number, count):
        threading.Thread.__init__(self)
        self.name = name
        self.num = number
        self.count = count

    def run(self):
        print("%s is running." % self.name)
        threadLock.acquire()
        test_set(self.num, self.count)
        test_print(self.name)
        print('%s执行完了后，最终的lists为：%s' % (self.name, lists))
        threadLock.release()

def test_print(name):
    for list in lists:
        print('%s当前正在打印的值为：%d' % (name, list))

def test_set(num, delay):
    len_list = len(lists)
    for i in range(0, len_list):
        time.sleep(delay)
        lists[i] = num

threadLock = threading.Lock()
threads = []

thread1 = myThread('Thread1', 3, 1)
thread2 = myThread('Thread2', 5, 1)
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("退出主进程")