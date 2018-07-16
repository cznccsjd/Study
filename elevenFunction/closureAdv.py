#coding:utf-8
"""
闭包用法，高级部分
下面的例子说明了如何能通过使用hjuudeefunc_closure属性来追踪闭包变量
"""
#!/usr/bin/env python

output = '<int %r id=%#0x val=%d>'
w = x = y = z = 1

def f1():
    x = y = z = 2

def f2():
    y = z = 3

    def f3():
        z = 4
        print output% ('w', id(w), w)
        print output% ('x', id(x), x)
        print output% ('y', id(y), y)
        print output% ('z', id(z), z)
    """
    17-22行，这个部分描绘了f3()的定义，创建一个局部的变量x。接着显示w、x、y、z，这4个变量
    从最内部作用域逐步向外的追踪到的。在f3()、f2()或f1()中都是找不到变量w的，所以这是个全局变量。在f3()或者f2()中，
    找不到变量x，所以来自f1()的闭包变量。相似的y是一个来自f2()的闭包变量。最后,z是f3()的局部变量。
    """
    clo = f3.func_closure
    if clo:
        print "f3 closure vars:", [str(c) for c in clo]
    else:
        print "no f3 closure vars"
    f3()

    clo = f2.func_closure
    if clo:
        print "f2 closure vars:",[str(c) for c in clo]
    else:
        print "no f2 closure vars"
    # f2()

clo = f1.func_closure
# print "clo：", clo
if clo:
    print "f1 closure vars:", [str(c) for c in clo]
else:
    print "no f1 closure vars"
# f1()
f2()
'42-45行，main()中剩余的部分尝试去显示f1()的闭包变量，但是什么都不会发生因为在全局域和f1()的作用域' \
'之间没有任何的作用域--没有f1()可以借用的作用域，因此不会创建闭包--所以第42行的条件表达式永远不会求得' \
'True。这里的代码仅仅是有修饰的目的。'
