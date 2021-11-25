#coding:utf-8
'''
将函数作为参数传递给另一个函数
装饰器的原理下面代码这样的
'''
def hi():
    return "Hi decoration!"

def doSomeThingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())

doSomeThingBeforeHi(hi)