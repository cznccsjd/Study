#coding:utf-8
"""
函数式编程举例
函数式变成的另一个有用的应用出现在调试和性能测量方面上。你正在使用需要每晚都被完全测试或
通过回归，或需要给对潜在改善进行多次迭代计时的函数来工作。你所要做的就是创建一个设置测试环境的诊断函数，然后
对有疑问的地方，调用函数。因为系统应该是灵活的，所以想teste函数作为参数传入。那么这样的函数对，timeit()和testit()，可能会对
如今的软件开发者有帮助。
    我们现在将展示这样的一个testit()函数的例子的源代码，我们将留下timeit()函数作为读者的练习；
    该模块给函数提供了一个执行测试的环境。testit()函数使用了一个函数和一些参数，然后在异常处理的监控下，用给定的参数调用了那个函数。如果函数成功的完成，会返回True和函数的返回值给调用者。
任何失败都会导致False和异常的原因一同被返回。
    （Exception是所有运行时刻异常的根类）
"""
#!/usr/bin/env python

def testit(func, *nkwargs, **kwargs):
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as err:
        result = (False, str(err))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_' * 20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            # print retval
            if retval[0]:
                print '%s(%s)=' % (eachFunc.__name__, 'eachVal'), retval[1]
            else:
                print '%s(%s)=FAILED:'%(eachFunc.__name__,'eachVal'),retval[1]

if __name__ == '__main__':
    test()