#coding:utf-8
"""
python第四次作业
"""

class One():
    """
    1【函数默认参数】定义一个函数，输出姓名和年龄，年龄默认29岁，并调用这个函数，输出
    （1）姓名：lili 年龄：29    
    （2）姓名：hanmeimei 年龄：13 
    """
    def info(self,name = '', age = 29):
        print "姓名:%s 年龄:%d" % (name, age)

    def triangle(self):
        """
        2【函数参数和返回值】定义一个函数，计算三角形的面积
        三角形面积公式：s = 1/2(a*h)    底乘高 除以 2 = 三角形面积
        :return: 
        """
        a = input("请输入三角形的底边长度：")
        h = input("请输入三角形的高：")
        s = (a * h) / 2
        print "三角形的面积是:", s

    def third(self):
        """
        3【可变对象做参数】定义一个函数，参数为list类型，功能在list末尾追加list1=[1,2,3,4]
        :return: 
        """
        list = []
        list1 = [1,2,3,4]

        #输入任意不为数字的字符，即可停止生成列表
        while(1 > 0):
            try:    #下面的判断，只适用于Python2.7，  3.6不适用
                i = input("请输入任意数字，以便生成列表，输入任何不为数字的字符，即可跳出循环：")
            except:
                break
            list.append(i)
            print list

        #在list末尾追加list1=[1,2,3,4]
        list.extend(list1)

        print "最终列表为:", list


class Fourth():
    '''
    4【关键字参数】定义一个函数，有多个参数，输出姓名，年龄，性别；调用时将参数顺序打乱（年龄，性别，姓名）分别赋值
    '''
    def key(self, name, age, sex):
        print "姓名：",name
        print "年龄：",age
        print"性别：",sex


class Nineth():
    """
    9【返回多个值】请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解
    """
    def auadratic(self,a,b,c):


if __name__ == '__main__':
    # One().info('lili')
    # One().info('hanmeimei', 13)
    # One().triangle()
    # One().third()
    # Fourth().key(age = 30, name = '51talk', sex = 'man')