#coding:utf-8
"""
习题 11.12    传递函数（例11.5的姊妹函数）
timeit()会带一个函数对象（和参数一起）并计算出用了多少时间来执行这个函数，而不是测试执行时的错误。返回
下面的状态：函数返回值、消耗的时间。你可以用time.clock()或者time.time()，无论哪一个给你提供了较高的精度（一般
的共识是在POSIX上用time.time()，在win32系统上用time.clock()）。注意：timeit()函数与timeit模块不相关
"""
#!/usr/bin/env python

import time

def timeit(func, *nkwargs, **kwargs):
    try:
        ret = func(*nkwargs, **kwargs)
        result = (True, ret)
    except Exception as err:
        result = (False, err)
    return result

def test():
    funcs = (int, long, float)
    args = (1234, 12.34, '12.34', '1234')
    for eachFunc in funcs:
        print '-*'*20
        for eachArg in args:
            #程序执行前的时间
            time_begin = time.clock()
            ret = timeit(eachFunc, eachArg)

            if (ret[0]):
                print "%s(%s):%s" % (eachFunc, eachArg, ret[1])
            else:
                print "FAILED!%s(%s):%s" % (eachFunc, eachArg, ret[1])

            # 程序执行完的的时间
            time_end = time.clock()
            # 计算方法执行完后的时间差
            time_diff = time_end - time_begin
            print '时间差，函数写的还是有问题:', time_diff

def aaa():
    time_begin = time.clock()
    print time_begin
    print time.time()

if __name__ == '__main__':
    test()
    # aaa()


