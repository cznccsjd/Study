#coding:utf-8

"""
多线程和单线程对比
下面的例子中，先在for循环中，一次调用fib() fac() sum()三个函数，再用多线程的方式调用三个函数，可以直观的比对单线程和多线程的差异
"""

from seven_threading_Thread import MyThread
from time import sleep, ctime

# 斐波那契数列
def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-1) + fib(x-2))

# 阶乘
def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

# 累加
def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print("*** SINGLE THREAD")
    for i in nfuncs:
        print("starting%s at:%s" %(funcs[i], ctime()))
        print(funcs[i](n))
        print(funcs[i].__name__, ' finished at:', ctime())

    print("\n***MULTIPLE THREADS")
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].get_result())

    print("all DONE")

if __name__ == '__main__':
    main()

# print(fib(3))
# print(fac(6))
# print(sum(6))