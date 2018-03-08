#coding:utf-8
"""
3.4.1 模块结构和布局
    （1）起始行（unix）
    通常只有在类Unix环境下才使用起始行，有起始行就能仅输入脚本名字来执行脚本，无需直接调用解释器；
    #/usr/bin/env python
    （2）模块文档（文档字符串）
    简单介绍模块的功能及重要全局变量的含义，模块外可通过module.__doc__访问这些内容
    *this is a test module*
    （3）模块导入
    import sys
    import os
    （4）函数定义
    debug = True
    （5）类定义
    class FooClass (object):
        "Foo class"
        pass
    （6）函数定义
    def test():
        "test function"
        foo = FooClass()
        if debug:
            print "ran test()"
    （7）主程序
    if __name__ == '__main__':
        test()
        
    #核心笔记：__name__指示模块应如何被加载
        *如果模块是被导入，__name__的值为模块名字；
        *如果模块是被直接执行，__name__的值为'__main__'
"""