#coding:utf-8
#!/usr/bin/env python

#接收一个数值参数，通过内建函数type()来确认数值的类型
def displayNumType(num):
    #num = raw_input("please enter:")
    print num, 'is',
    if isinstance(num, (int, long, float,complex)):
        print 'a number of type:', type(num),__name__
    else:
        print "not a number at all"

#更细致优化
def displayNumTypeAdv(num):
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

if __name__ == '__main__':
    nu = 23.23
    displayNumType(nu)
    displayNumTypeAdv(nu)


"""
原文（page69-70）（4.6.4）还有对该功能代码性能优化的介绍，推荐查看
"""