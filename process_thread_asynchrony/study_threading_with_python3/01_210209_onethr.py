#coding:utf-8

"""
创建2个事件循环，一个睡眠4秒（loop0());另一个睡眠2秒(loop1())
"""

from time import sleep, ctime

def loop0():
    print('start loop 0 at:')