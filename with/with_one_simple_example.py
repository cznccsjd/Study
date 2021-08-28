#coding:utf-8

"""
学习with
1、首先要确定什么样的对象可以使用with语句？
实现了上下文协议的对象就可以使用with语句。对于实现了上下文协议的对象，我们通常称为上下文管理器。

2、一个上下文管理器如何实现上下文协议呢？
实现了__enter__和__exit__这两个方法就是实现了上下文协议。
"""

class Test:
    enter = 'Enter...'
    exit = 'Exit...'

    def __enter__(self):
        print(self.enter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.exit)

with Test():
    print('This is test function')