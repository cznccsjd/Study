#coding:utf-8
#!/usr/bin/env python
"""
这个例子通过显示函数执行的时间“装饰”了一个（没有用的）函数。这是一个“时戳装饰”，与16章中谈论的时戳服务器非常相似；
这个装饰器（以及闭包）示范表明装饰器仅仅是用来“装饰”（或者修饰）函数的包装，
返回一个修改后的函数对象，将其重新赋值原来的标识符，并永久失去对原始函数对象的访问。
********* 下面的函数报错，也可以通过Python2.4中的“What's New in Python 2.4”中的文档，来阅读更多关于装饰器的内容
"""
from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print "[%s] %s() called" % (ctime(), func.__name__)
        print 'func()是：', func
        return func()
    return wrappedFunc()

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()