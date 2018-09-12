#coding:utf-8
# from imptee import foo, show
# show()
# foo = 123
# print 'foo from impter:', foo
# show()


# 上面代码，从被导入者的观点看，foo的变量值没有改变，即便我们修改了它
# 解决方案如下：

import imptee
imptee.show()
imptee.foo = 123
print 'foo from imptee:', imptee.foo
imptee.show()