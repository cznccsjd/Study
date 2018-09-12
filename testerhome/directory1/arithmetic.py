#coding:utf-8
'''
计算的算法
'''

class Arithmetic:
    def jia(self,x, y):
        return x + y

    def jian(self,x,y):
        if x > y:
            return x - y
        else:
            return y - x

    def cheng(self,x,y):
        return abs(x*y)

    def chu(self,x,y):
        try:
            return x/y
        except ZeroDivisionError,e:
            e = "除数不能为零！"
            print e


if __name__ == '__main__':
    print Arithmetic().chu(4,0)