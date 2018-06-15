#coding:utf-8
"""
11.7  函数式编程
"""

# ######    简单的函数式例子  通过functools模块下的partial()函数了创建PFA
from operator import add, mul
from functools import partial
import Tkinter

def testOne():
    addTest = partial(add, 1)   #等同于 addTest(x) == add(1, x)
    mulTest = partial(mul, 100) #等同于 mulTest(x) == mul(100, x)

    # print addTest(10)
    # print mulTest(5)

    '''
    上面例子或许不能看到PFA的威力，但是我们不得不从某个地方开始。当调用带许多参数的函数的时候，
    PFA是最好的方法。使用带关键字参数的PFA也是较简单的，因为能显示给出特定的参数，要么作为curried参数，
    要么作为那些在运行时刻传入的变量，并且我们不需担心顺序，下面的一个例子来自Python文档中关于在应用程序中使用，
    在这些程序中需要经常将二进制（作为字符串）转换成为整型；
    '''
    baseTwo = partial(int,base=2)
    baseTwo.__doc__ = 'Convert base 2 string to an int.'

    print baseTwo('10010')
    """
    上面这个例子使用了int()内建函数并将base固定位2来指定二进制字符串转化。现在我们没有多次用相同的的第二参数（2）来调用int()， \
    比如（'10010',2），相反，可以只用带一个参数的新baseTwo()函数。接着给新的（部分）函数加入了新的文档并有一次很好的使用了“函数属性”，这是
    很好的风格。要注意的是这里需要关键字参数base
    """


######  警惕关键字
"""
如果创建了不带base关键字的片函数，比如，baseTwo-BAD = partial(int,2)，这可能会让参数以错误的顺序传入int()，
因为固定参数的总是放在运行时刻参数的左边，比如baseTwoBAD(x) == int (2,x)。如果调用它，会将2作为需要转化的数字，
base作为‘10010’来传入，接着产生一个异常；
由于关键字放置在恰当的位置，顺序就得固定下来，因为，如你所知，关键字参数总是出现在形参之后，所以baseTwo(x)== int(x, base=2)
"""

########    简单GUI类的例子
"""
PFA也扩展到所有可调用的东西，如类和方法。一个使用PFA的优秀的例子是提供了“部分GUI模范化”。GUI小部件通常有很多的参数，
如文本、长度、最大尺寸、背景和前景色、活动或者非活动等等。如果想要固定其中的一些参数，如让所有的文本标签为蓝底白字，你可以
准确地以PFA的方式，自定义为相似对象的伪模版。
这是较有用的偏函数应用的例子，或者更准确地说，“部分类实例化”
"""
def testTwo():
    root = Tkinter.Tk()
    MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
    b1 = MyButton(text='Button 1')
    b2 = MyButton(text='Button 2')
    qb = MyButton(text='QUIT', bg='red', command=root.quit)

    b1.pack()
    b2.pack()
    qb.pack(fill=Tkinter.X, expand=True)
    root.title('PFAS!')
    root.mainloop()


if __name__ == '__main__':
    testTwo()