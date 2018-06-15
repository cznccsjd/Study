#coding:utf-8
"""
11.8.4  简单的闭包例子
模拟一个计数器，同样也通过将整型包裹为一个列表的单一元素来模拟使整型易变
"""
def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr

"""
counter()做的唯一一件事就是接受一个初始化的值来开始计数，并将该值赋给列表count唯一一个成员。然后
定义一个incr()的内部函数。通过在内部使用变量count,我们创建了一个闭包，因为它现在携带了整个counter()
作用域。incr()增加了正在运行的count然后返回它。然后最后的魔法就是counter()返回了一个incr,
一个（可调用的）函数对象。如我们交互的运行这个函数，将得到如下的输出--注意这个看起来和实例化一个counter对象
并执行这个实例有多么相似；
"""