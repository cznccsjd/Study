#coding;utf-8
"""
11.3.6 deco.py，使用闭包和装饰器的简单例子；接下来是稍微高级点的例子，来演示闭包的真正威力；
应用程序“logs”函数调用。用户选择是要在函数调用之前或者之后，把函数调用写入日志。如果选择贴日志，执行时间也会显示出来。
这个例子演示了带参数的装饰器，该参数最终决定拿一个闭包会被用的，这也是闭包的威力的特征；
"""

from time import time

def logged(when):
    def log(f, args, kargs):
        print '''Called:
functions:%s
agrs:%r
kargs:%r''' % (f, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapped(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "time delta:%s" % (time()-now)
        return wrapper

    try:
        return {"pre": pre_logged,
                "post": post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'

@logged("post")
def hello(name):
    print "Hello,", name

hello("world!")