#coding:utf-8
"""
一个将函数作为参数传递，并在函数体内调用这些函数，更加实际的例子。
这个脚本用传入的转换函数简单讲一个序列的数转化为相同的类型。
特别地，test()函数传入一个内建函数int()、long()或float()来执行转换；
"""
def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45.67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)