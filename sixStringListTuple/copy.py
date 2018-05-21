#coding:utf-8
"""
深浅拷贝
"""

"""
例子：假设创建一对小夫妻的通用档案，分别拷贝，使用两种拷贝对象的方式，一种使用切片操作，
另一种使用工厂方法，为了区分3个不同的对象，我们使用id()内建函数来显示每个对象的标识符；
"""
person = ['name',['savings',100.00]]
hubby = person[:]   #通过切片拷贝了person
wifey = list(person)    #通过方法进行拷贝

print person, hubby, wifey
print [id(x) for x in person, hubby, wifey]     #打印id，大家的id是不一样的


hubby[0] = 'joe'
wifey[0] = 'jane'
print hubby, wifey

hubby[1][1] = 50.00
print hubby, wifey
"""
wifey的值变化是因为，仅仅做了一个浅拷贝。对一个对象进行浅拷贝其实是新创建了一个类型跟元对象一样，
其内容是原来对象元素的引用，这个拷贝的对象本身是新的，但是他的内容不是。序列类型对象的浅拷贝是默认类型拷贝，
并可以以下几种方式实施：1）完全切片操作[:]；2）利用工厂函数，比如list()、dict()等；3）使用copy模块的copy函数；
"""
"""
名字没有改变，是因为这两个列表中，第一个对象是不可变的（字符串类型），而第2个是可变的（一个列表）。
进行浅拷贝时，字符串被显示的拷贝，并新创建了一个字符串对象，而列表元素只是把它的引用复制了一下，并不是它的成员。
所以改变名字没有任何问题，但是更改他们的银行账号的任何信息都会引发问题。查看一下每个列表元素的对象ID值；
"""
print [id(x) for x in hubby]
print [id(x) for x in wifey]


"""
深拷贝，使用copy.deepcopy()
"""



