#coding:utf-8

class Wang():
    def first(self):
        '''
        # 1、python代码块的缩进非常严格，请写出主要的几种缩进，并养成自己的缩进风格。
        :return: 
        '''
        print "1、Python代码块缩进的写法：\n" \
              "\t1）单个制表符\n" \
              "\t2)两个或四个空格\n" \
              "\t上面的答案抄的王平的\n"

    def second(self):
        """
        2、python注释的使用，并指出各自区别，什么时候用什么样的注释。
        :return: 
        """
        print "2、python的注释有以下几种：\n" \
              "\t1) #号注释，eg：#!/usr/bin/env python\n" \
              "\t2) ""文档字符串注释，文档字符串可以在运行时访问，也可以用来自动生成文档\n" \
              "\t有时间还是可以抄王平的答案，写的很详细!!!\n"


    def third(self):
        """
        3、请写出python的标准数据类型，并举例说明
        :return: 
        """
        print "3、python的标准数据类型：\n" \
              "\t1)Number（数字）(int、float、bool、set？？)\n" \
              "\t2)String（字符串）（string）\n" \
              "\t3)List（列表）(list[])\n" \
              "\t4)Tuple（元组）(tuple())\n" \
              "\t5)Sets（集合）(set)\n" \
              "\t6)Dictionary（字典）(dic{})\n" \
              "  说明：不可变数据(Number、String、Tuple、Sets)，可变数据(List、Dictory)\n"

    def fourth(self):
        """
        # 4、编写一段代码，如果age 大于等于 18 ，输出结果为 成人
        :return: 
        """
        print "# 4、编写一段代码，如果age 大于等于 18 ，输出结果为 成人\n"
        try:
            age = input("please input age:")
        except (NameError,SyntaxError):
            print "要输入数字好不"
            Wang().fourth()

        while(1>0):
            if age >= 18:
                print "Adult"
            else:
                print "Not Adult"

            again = raw_input("输入Y继续运行，否则输入n：:")
            if again in ('Y','y'):
                Wang().fourth()
            else:
                pass
            break

    def fifth(self):
        """
        5、if语句什么情况下会执行，什么情况下会执行。
        :return: 
        """
        print "5、if语句后面的等式成立后，会立刻执行，否则执行elif或者else；\n"

    def sixth(self):
        """
        # 6、请使用for循环编写一段程序，状态值有[1 ,3 ,2, 0]如果status =2，打印当前status值，然后跳出本次循环，
            # 进行下一次循环；如果状态值为0，则打印当前status值，然后终止循环。
            # 如果是其他值，则正常循环，并打印status值，和“运行正常”文案。
        :return: 
        """
        list = [1,3,2,0]

        for i in range(0,4):
            if list[i] == 0:
                print "status:\n", list[i]
                print "Now,status = 0,discontinue"
                break
            elif list[i] == 2:
                print "status:\n", list[i]
                print "END"
                continue
            else:
                print "status:", list[i]
                print "continue\n"


    def seventh(self):
        """
        # 7、请使用while循环编写一段程序，如果name='python',password='123456'则打印：登录成功；
            # 否则登录失败。5次登录机会（不用管超过5次显示什么）。
        :return: 
        """
        num = 0
        while(num < 5):
            num = num + 1
            name = raw_input("please input your account:")
            passwd = raw_input("please input your password:")

            if name == "python" and passwd == "123456":
                print "login success"
            else:
                print "login failed(count %d), please relogin!!\n" % num

    def eighth(self):
        """
        # 8、输出格式化的字符串（使用% 或者.format都行），需要格式化的内容- xx，实现以下内容：
            # 我姓名是xx，我年龄是xx，我身高是xx(这里保留两位小数)
        :return: 
        """
        name = raw_input("My name is:")
        try:
            age = input("My age is:")
            height = input("My height is(m):")
        except SyntaxError,e:
            print "SyntaxError:只能输入数字好不"
            Wang().eighth()

        print "My name is %s, my age is %d, my height is %0.2f" % (name, age, height)

    def ninth(self):
        """
        # 9、从1-100里面，取出所有偶数放到一个list里面
        :return: 
        """
        list = []

        for i in range(1,101):
            if i % 2 == 0:
                list.append(i)
        print list

    def tenth(self):
        """
        # 10、面试题，
        # 1）请问list和tuple有什么区别；
        # 2）python中哪些是可变对象，哪些是不可变对象。
        :return: 
        """
        print "10.1 list和tuple的区别：\n" \
              "\t列表元素用[]包裹，元素的个数及元素的值是可以改变的；" \
              "元组元素用()包裹，不可以改变；" \
              "元组可以看成是只读的列表；\n"
        print "10.2 python中的可变对象:列表和字典；\n" \
              "\tpython中不可变对象：字符串、数字、元组、集合"


if __name__ == '__main__':
    Wang().first()
    Wang().second()
    Wang().third()
    Wang().fourth()
    Wang().fifth()
    Wang().sixth()
    Wang().seventh()
    Wang().eighth()
    Wang().ninth()
    Wang().tenth()