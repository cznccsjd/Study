#coding:utf-8
"""
非关键字可变长参数（元组）
带元组（或者非关键字可变长参数）的函数普通语法如下：
def function_name([formal_args,] *vargs_tuple):
    "function_documentation_string"
    function_body_suite
星号操作符之后的形参将作为元组传递给函数，元祖保存了所有传递给函数的“额外”的参数（匹配了所有位置和具名参数后剩余的）。
如果没有给出额外的参数，元组为空。
只要在函数调用时给出不正确的函数参数数目，就会产生一个TypeError异常。通过末尾增加一个可变的参数列表变量，
我们就能处理当超出数目的参数被传入函数的情形，因为所有的额外（非关键字）参数会被添加到变量参数元组（额外的
关键字参数需要关键字变量参数）。正如所料的那样，由于和未知参数必须放在关键字参数之前一样的原因，所有的形式参数
必须先于非正式的参数之前出现。
"""
def tupleVarArgs(arg1,arg2='defaultB',*theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg2

    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg
    print '\n'


# tupleVarArgs('abc')
# tupleVarArgs(23, 4.56)
tupleVarArgs('abc', 123, 'xyz', 456.789)