#coding:utf-8
"""
关键字变量参数（字典）
在我们有不定数目的或者额外集合的关键字的情况中，参数被放入一个字典中，字典中间为参数名，
值为相应的参数值。为什么一定要是字典呢？因为每个参数--参数的名字和参数值--都是承兑给出，用
字典来保存这些参数自然就最适合不过了。
这给出使用变量参数字典来应对额外关键字的函数定义的语法：
def function_name([fornal_args,][*vargst,] **vargsd):
    function_documentation_string
    function_body_suite
为了区分关键字参数和非关键字非正式参数，使用了双星号（**）。**是呗重载了以便不与幂运算发生混淆。关键字
变量参数应该为函数定义的最后一个参数，带**。
我们现在展示一个如果使用字典的例子：
"""
def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' %(eachXtrArg, str(theRest[eachXtrArg]))

# dictVarArgs(1220, 740.0, c='grail')
# dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
# dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))

"""
关键字和非关键字可变长参数都有可能用在同一个函数中，只要关键字字典是最后一个参数
悲切非关键字元组先于它之前出现，例如下面的例子
"""
def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s':%s" % (eachKW, kw[eachKW])

# newfoo('wolf', 3, 'projects', freud=90, qamble=30)
"""
调用带有可变长参数对象函数
"""
# '使用旧风格分别列出所有的参数，甚至跟在所有形式参数之后的变长参数'
# newfoo(10, 20, 30, 40, foo=50, bar=60)
# '将非关键字参数放在元组中，将关键字参数放在字典中，而不是逐个列出变量参数'
# newfoo(2, 4, *(6, 8), **{'foo':10, 'bar':12})
# '在函数调用之外来创建我们的元组和字典'
aTuple = (6, 7, 8)
aDict = {'z': 9}
newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)