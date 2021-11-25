#coding:utf-8
'''
在函数中嵌入装饰器
我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。
'''
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as open_file:
                # 现在将日志打到指定的logfile
                open_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

# 现在出现了一个叫做out.log的文件，存储着上面的字符串
print(myfunc1.__name__)
myfunc1()