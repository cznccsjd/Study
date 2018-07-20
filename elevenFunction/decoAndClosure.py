#coding:utf-8
"""
闭包和装饰器深入学习，通过该文件，逐步了解闭包和装饰器
"""
'''
函数是Python世界里的一级类对象
'''
# 在Python里函数和其他东西一样都是对象
# def foo():
#     pass
# print"打印 foo:",foo
# print "打印foo.__class__:",foo.__class__
# print '打印foo():',foo()
# 从上面的语句可以看出，定义的函数居然有属性，在python中，函数只是一些普通的值而已，和其他的值一模一样。这就是说，
# 你可以把函数像参数一样传递给其他的函数或者说从函数里面返回函数。可以参考下面的例子：
# def add(x, y):
#     return x + y
# def sub(x, y):
#     return x - y
# def apply(func, x, y):  #1
#     return func(x, y)   #2
# print '把add当成参数传给apply：',apply(add, 2, 1)       #3
# print '把sub当成参数传给apply：',apply(sub, 2, 1)
# 上面的例子，add和sub是非常普通的两个python函数，接受两个值，返回一个计算后的结果值。再#1处，准备接受一个函数的变量，
# 只是一个普通的变量而已，和其他变量一样。在#2处，调用传进来的函数：“()代表中调用的操作并且调用变量包含的值。在#3处，传递的函数并没有什么特殊的语法”。函数
# 的名称只是和其他变量一样的标识符而已。


'''
把函数当作返回值
'''
# def outer():
#     def inner():
#         print "Inside inner"
#     return inner  #1
# foo = outer()       #2
# print 'foo的值：',foo
# print 'foo()的值：',foo()
# 上面的例子中，#1处恰好是函数标识符的变量inner作为返回值返回出来。这并没有什么特殊的语法：‘把函数inner返回出来，
# 否则他根本不可能会被调用到# ’每次函数outer被调用的时候，函数inner都会被重新定义，如果他不被当做变量返回的话，每次
# 执行过后他将不复存在。
# 在#2处我们捕获返回值 - 函数inner，将它存在一个新的变量foo里。我们能够看到，当对变量foo进行求职，他确实包含函数inner，
# 而且我们能够对他进行调用。初次看出来可能会觉得有点奇怪，但是理解起来并不困难。


'''闭包'''
# def outer():
#     x = 1
#     def inner():
#         print x     #1
#     return inner
# foo = outer()
# print 'foo.func_closure的值：',foo.func_closure
# 上面函数outer被调用的时候，函数inner都会被重新定义。现在变量x的值不会变化，所以每次返回的函数inner会是同样的逻辑
# 将函数稍微改动一下
# def outer(x):
#     def inner():
#         print x #1
#     return inner
# print1 = outer(1)
# print2 = outer(2)
# print 'print1()的值：',print1()
# print 'print2()的值：',print2()
# 上面的例子可以看到闭包 - 被函数记住的封闭作用域 - 能够被用来创建自定义的函数，本质上来说是一个硬编码的参数。
# 事实上我们并不是传递参数1或者2给函数inner，我们实际上是创建了能够打印各种数字的各种自定义版本
# 闭包单独拿出来就是一个非常强大的功能， 在某些方面，你也许会把它当做一个类似于面向对象的技术：outer像是给inner服务的构造器，x像一个私有变量。


# 闭包写个高大上的装饰器
'''
装饰器
'''
# 装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数。我们一步步从简到繁来瞅瞅
# def outer(some_func):
#     def inner():
#         print "before some_func"
#         ret = some_func()   #1
#         return ret + 1
#     return inner
# def foo():
#     return 1
#     pass  #使用pass，就把上面的return注释掉
# decorated = outer(foo)  #2
# decorated()
# print decorated()
#     仔细看上面这个装饰器的例子，我们定义了一个函数outer，他只有一个some_func的参数，在里面我们定义了一个嵌套函数inner。inner会打印一串字符串，然后调用some_func，
# 在#1处得到他的返回值。在outer每次调用的时候some_func的值可能会不一样，但是不管some_func的值如何，我们都会调用它。最后inner返回some_func() + 1的值 ——我们通过调用在#2处
# 存储的变量decorated里面的函数，能看看到被打印出来的字符串和返回值2，而不是期望中调用函数foo得到的返回值1.
#     我们可以认为变量decorated是函数foo的一个装饰版本，一个加强版本。事实上如果打算写一个有用的装饰器的话，我们可能会想愿意用装饰版本完全取代原先的函数foo，这样我们总是会得到我们
# 的”加强版“foo。想要达到这个效果，完全不需要学习新的语法，简单地赋值给变量foo就行了：
# foo = outer(foo)
# decorated = outer(foo)  #2
# decorated()
# 讲真，看不懂上面这三行代码再做什么，搞不懂，那就先不搞了

# 想象我们有一个库，这个库能够提供类似坐标的对象，也许它们仅仅是一些x和y的坐标对。不过可惜的是这些坐标对象不支持数学运算符，而且我们也不能对源代码进行修改，因此也就不能直接加入运算符的支持。
# 我们将会做一系列的数学运算，所以我们想要能够对两个坐标对象进行合适加减运算的函数，这些方法很容易就能写出：
# class Coordinate(object):
#     def __init__(self, x, y):
#         """
#         初始化x, y（自己定义的）
#         :param x:
#         :param y:
#         """
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         """
#         我也不知道干啥的，看功能就是返回坐标值
#         :return: Coord:{x,y}
#         """
#         return "Coord:" + str(self.__dict__)
#
# def add(a, b):
#     """
#     function add
#     :param a:
#     :param b:
#     :return: Coordinate()类的返回值
#     """
#     return Coordinate(a.x + b.x, a.y + b.y)
# def sub(a, b):
#     """
#     function sub
#     :param a:
#     :param b:
#     :return:
#     """
#     return Coordinate(a.x - b.x, a.y - b.y)
#
# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
# three = Coordinate(-100, -100)
# print one,two,three
#
# # print one, two
# print add(one, two), sub(one, two)
# 我们期望在不更改坐标对象one, two, three的前提下one减去two的
# 值是{x: 0, y: 0}，one加上three的值是{x: 100, y: 200}。与其给每个方法
# 都加上参数和返回值边界检查的逻辑，我们来写一个边界检查的装饰器！
# def wrapper(func):
#     """
#     这个方法。。。
#     :param func:
#     :return:
#     """
#     def checker(a, b):  #1
#         """
#         具体操作的方法，将负数变为0
#         :param a:
#         :param b:
#         :return:
#         """
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y >0 else 0)
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y >0 else 0)
#         ret = func(a, b)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#         return ret
#     return checker
# add = wrapper(add)
# # sub = wrapper(sub)
# print 'add:',add
# # print 'sub:',sub
# # print sub(one, two)
# print add(one, three)
#     这个装饰器能想先前的装饰器例子一样进行工作，返回一个经过修改的函数，但是在这个例子中，它能够对函数的输入参数和返回值做一些非常有用的
# 检查和格式化工作，将负值的x和 y替换成0。
#     显而易见，通过这样的方式，我们的代码变得更加简洁：将边界检查的逻辑隔离到单独的方法中，然后通过装饰器包装的方式应用到我们需要进行检查的
# 地方。另外一种方式通过在计算方法的开始处和返回值之前调用边界检查的方法也能够达到同样的目的。但是不可置否的是，使用装饰器能够让我们以最
# 少的代码量达到坐标边界检查的目的。事实上，如果我们是在装饰自己定义的方法的话，我们能够让装饰器应用的更加有逼格。


'''
使用 @ 标识符将装饰器应用到函数
'''
# 上面的例子里，我们将原本的方法用装饰后的方法代替
# add = wrapper(add)
# 这种方式能够在任何时候对任意方法进行包装。但是如果我们自定义一个方法，我们可以使用@进行装饰：
# @wrapper
# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)
# 需要明白的是，这样的做法和先前简单的用包装方法替代原有方法是一模一样的，Python只是加了一些语法让装饰的行为更加直接明确和优雅一点
# 用带@标识符的装饰器，重构代码,hahahahha，写出来了
# class Coordinate(object):
#     """
#     设置坐标输出格式
#     """
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord:" + str(self.__dict__)
#
# def wrapper(func):
#     """
#     装饰器函数
#     :param func:
#     :return:
#     """
#     def check(a, b):
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
#         ret = func(a, b)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y >0 else 0)
#         return ret
#     return check
#
# @wrapper
# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)
#
# @wrapper
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)
#
# one = Coordinate(100, -200)
# two = Coordinate(-300, 500)
#
# print add(one, two)
# print sub(one, two)


'''
*args and **kwargs
'''
#     我们已经完成了一个有用的装饰器，但是由于硬编码的原因它只能应用在一类具体的方法上，这类方法接收两个参数，传递给闭包捕获的函数。如果
# 我们想实现一个能够应用在任何方法上的装饰器要怎么做呢？再比如，如果我们要实现一个能应用在任何方法上的类似于计数器的装饰器，不需要改变
# 原有方法的任何逻辑。这意味着装饰器能够接受拥有任何签名的函数作为自己的被装饰方法，同时能够用传递给它的参数对被装饰的方法进行调用。
#     非常巧合的是Python正好有支持这个特性的语法。可以阅读 Python Tutorial 获取更多的细节。当定义函数的时候使用了*，意味着那些通过位置传递的参数
# 将会被放在带有*前缀的变量中， 所以：
# def one(*args):
#     return args  #1
# print "one()的结果是：",one()
# print "one(1,2,3,4)的结果是：", one(1,2,3,4)
#
# def two(x, y, *args):   #2
#     return x, y, args
# print "two('a', 'b', 'c')的结果是：", two('a', 'b', 'c')
#     第一个函数one只是简单地讲任何传递过来的位置参数全部打印出来而已，你们能够看到，在代码#1处我们只是引用了函数内的变量args, *args仅仅只是用在函数定义
# # 的时候用来表示位置参数应该存储在变量args里面。Python允许我们制定一些参数并且通过args捕获其他所有剩余的未被捕捉的位置参数，就像#2处所示的那样。
#     *操作符在函数被调用的时候也能使用。意义基本是一样的。当调用一个函数的时候，一个用*标志的变量意思是变量里面的内容需要被提取出来然后当做位置参数被
# 使用。同样的，来看个例子：
# def add(x, y):
#     return x + y
# lst = [1, 3]
# print add(lst[0], lst[1])   #1
# print add(*lst) #2
#     #1处的代码和#2处的代码所做的事情其实是一样的，在#2处，python为我们所做的事其实也可以手动完成。这也不是什么坏事，*args要么是表示调用方法大的时候额外
# # 的参数可以从一个可迭代列表中取得，要么就是定义方法的时候标志这个方法能够接受任意的位置参数。
#     接下来提到的**会稍多更复杂一点，**代表着键值对的餐宿字典，和*所代表的意义相差无几，也很简单对不对：
# def foo(**kwargs):
#     print kwargs
# foo()
# foo(x = 1, y = 2)

# 当我们定义一个函数的时候，我们能够用**kwargs来表明，所有未被捕获的关键字参数都应该存储在kwargs的字典中。如前所诉，argshe kwargs并不是python语法的一部分，
# 但在定义函数的时候，使用这样的变量名算是一个不成文的约定。和*一样，我们同样可以在定义或者调用函数的时候使用**。
# dct = {'x':1, 'y':2}
# def bar(x, y):
#     print x + y
# bar(**dct)


'''
更通用的装饰器
'''
# 有了这招新的技能，我们随随便便就可以写一个能够记录下传递给函数参数的装饰器了。先来个简单地把日志输出到界面的例子：
def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)    #2
    return inner
# 请注意我们的函数inner，它能够接受任意数量和类型的参数并把它们传递给被包装的方法，这让我们能够用这个装饰器来装饰任何方法。
@logger
def foo1(x, y=1):
    return x * y
@logger
def foo2():
    return 2
print foo1(1)
print foo2()
# 随便调用我们定义的哪个方法，相应的日志也会打印到输出窗口，和我们预期的一样。