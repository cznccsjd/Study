#coding:utf-8
#!/usr/bin/env python

#接收一个数值参数，通过内建函数type()来确认数值的类型
def displayNumType(num):
    #num = raw_input("please enter:")
    print num, '\'s type:', type(num)
    print num, 'is',
    if isinstance(num, (int, long, float,complex)):
        print 'a number of type:', type(num).__name__
    else:
        print "not a number at all"

# 原版判断输入数字类型的代码，跟上面比有些不同
def displayNumTypeFir(num):
    print num, "is",
    if type(num) == type(0):
        print "an integer"
    elif type(num) == type(0L):
        print 'a long'
    elif type(num) == type(0.0):
        print 'a float'
    elif type(num) == type(0+0j):
        print 'a complex number'
    else:
        print 'not a number at all'

'''
优化2： 减少函数调用次数
displayNumTypeAdv(num)函数中，调用了两次type()，可以优化，提高程序的性能；
使用type模块，将检测的类型与一个已知类型进行比较，就可以只调用一次type()函数；
'''
import types
def displayNumTypeSec(num):
    if type(num) == types.IntType:
        print "an integer"
    else:
        print 'others'

'''
优化3：对象值比较 vs 对象身份比较
因为已经知道type(0)/type(10)/type(-100)都是同一个对象<type 'int'>(types.IntType也是这个对象)，所以没有
必要在浪费时间去获得并比较他们的值，直接比较对象本身是一个更好的方案
'''
def displayNumTypesThird(num):
    if type(num) is types.IntType:
        print "an integer"
    else:
        print "others"

'''
优化4：减少查询次数
上面的例子中，为了得到整型的对象类型，解释器不得不首先查找types这个模块名字，然后在
该模块的字典中查找IntType，通过使用from-import，可以减少一次查询
'''
from types import IntType
def displayNumTypesFour(num):
    pass

'''
优化5：惯例和代码风格
isinstance()接受一个或多个对象作为参数，比if语句更方便，更具可读性;
isinstance()可以接受一个类型对象的元祖作为参数，这样我们不必像使用type()那样写一堆的if-elif-else判断了；
'''
def displayNumTypesFive(num):
    if isinstance(num, int):
        pass


if __name__ == '__main__':
    nu = 23
    # displayNumType(nu)
    # displayNumTypeFir(nu)
    # displayNumTypeSec(nu)
    # displayNumTypesThird(nu)


