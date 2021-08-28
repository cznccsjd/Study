#coding:utf-8

"""
通常使用的时候，会在with后面加个as
as后面的变量，不是上下文管理器，可以参考本篇的例子
"""

class Test:
    enter = 'Enter...'
    exit = 'Exit...'

    def __enter__(self):
        print(self.enter)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.exit)

class TestTwo:
    enter = 'Enter...'
    exit = 'Exit...'

    def __enter__(self):
        print(self.enter)
        return TestTwo.enter

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.exit)

with Test() as obj:
    print("This is test function")
    print('def __enter__(self):不添加返回时，as obj中的obj值：',obj)

with TestTwo() as obj2:
    print("This is testTwo")
    print('def __enter__(self):有return后的obj2的值：', obj2)
