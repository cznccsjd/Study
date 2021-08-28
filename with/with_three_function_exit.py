#coding:utf-8
"""
def __exit__(self, exc_type, exc_val, exc_tb)
首先，定义_exit__函数时，四个形参缺一不可。如果参数不是四个，程序会报错；
一般__exit__都是用来做资源回收，除了这个功能外，他还能进行异常处理。exit四个参数中的后三个都与异常处理有关；
没有异常的情况下，__exit__后三个参数默认都是None。
下面的样例，让程序主动产生一个异常。
"""
class Test:
    enter = 'Enter...'
    exit = 'Exit...'

    def __enter__(self):
        print(self.enter)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'exc_type:{exc_type}')
        print(f'exc_val:{exc_val}')
        print(f'exc_tb:{exc_tb}')
        print(Test.exit)
        # 实际上__exit__只能返回False或者True；默认返回False
        #当return True时，__exit__方法执行完了后，with外部将不会抛出异常；
        # 当return False时，__exit__方法执行完了后，with外部还会抛出异常
        return True

    def run(self):
        print('fun execute')

with Test() as obj:
    1 / 0
    obj.run()


# 新增一个异常捕获，当__exit__返回False时，或者__exit__去掉return时，执行结果没有变化，
# 因为__exit__默认返回False
print('\n*****************************')
try:
    with Test() as obj2:
        1 / 0
        obj2.run()
except Exception:
    print('Exception captured')