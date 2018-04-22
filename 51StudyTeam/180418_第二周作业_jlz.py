#coding:utf-8
"""
python第二次作业；陈晓雪出题
"""
class Chen():
    '''
    每个方法为具体的第几题？
    '''
    def one(self):
        '''
        1.	list1 = ['Google', 'Runoob', 1997, 2000];
        2.	list2 = [1, 2, 3, 4, 5, 6, 7 ];
        3.	list3 = [12334]
        4.	输出list1的第一个值,list2的第2-5个值
        5.	将list1的第三个值变成2001,并输出新的list
        6.	删除list3的第三个元素并输出新的list
        7.	求list1的长度
        9.	List1+list2的新list6,输出新list6
        11.	list1的末尾插入’baidu’这个元素
        14.	删除list1中的四二个值       #没看懂题目是什么意思？？？
        15.	将list1倒序输出
        16.	将list2排序
        :return:
        '''
        list1 = ['Google', 'Runoob', 1997, 2000];
        list2 = [1, 2, 3, 4, 5, 6, 7];
        list3 = [1,2,3,3,4]

        print "4、list1的第一个值为:", list1[0],
        print "\tlist2的第2-5个值为：", list2[1:5]

        list1[2] = 2001
        print "5、将list1的第三个值变成2001,并输出新的list:",list1

        print "list3:", list3,
        del list3[2]
        print "6、删除list3的第三个元素并输出新的list:", list3

        print "7、求list1的长度为：", len(list1)

        print "9.	List1+list2的新list6,输出新list6为：", list1+list2

        list1.append('baidu')
        print "11.	list1的末尾插入’baidu’这个元素:", list1

        list1.reverse()     #list.reverse()和list.sort是在列表内部改变排序，没有返回值
        list2.sort()
        print "15、将list1倒序输出:", list1
        print "16、将list2排序:", list2

    def eight(self):
        '''
        8.	List4, list5 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200],求list4,list5的最大值
        :return:
        '''
        List4, list5 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
        print "8、List4最大值为：", max(List4),
        print "list5最大值为：", max(list5)

    def ten(self):
        '''
        10.	aTuple = (123, 'Google', 'Runoob', 'Taobao'),将这个元组装换成list
        :return:
        '''
        list = []
        aTuple = (123, 'Google', 'Runoob', 'Taobao')
        i = 0
        for tuple in aTuple:
            # list1 = tuple
            # list = list.append(-1, list1)
            # print tuple
            list[i] = tuple
            # print list
            i = i + 1
        print list

    def twelve(self):
        '''
        12.	aList = [123, 'Google', 'Runoob', 'Taobao', 123];计算’123在alist中出现的次数
        13.	计算runoob在list中的索引位置
        :return:
        '''
        aList = [123, 'Google', 'Runoob', 'Taobao', 123];
        print "12、123在alist中出现的次数：", aList.count(123)
        print "13.	计算runoob在list中的索引位置:", aList.index('Runoob')

    def twentyOne(self):
        '''
        21.	计算并输出0-10的质数,提示,质数:只有1和他本身两个因数,只能被1和他本身整除
        概念：质数又称素数。指在一个大于1的自然数中，除了1和此整数自身外，没法被其他自然数整除的数。
        解体思路：
        1、(除数 % 被除数 != 0) 的个数 等于 除数 - 2 即可（质数可以被1和自己本身整除）
        2、(除数 % 被除数 == 0) 的个数 小于 2 （质数只可以被自己本身和1整除）
        :return:
        '''
        # num = input("输入0-10间")
        nums = range(1,10)
        list = []
        for num in nums:
            count = 0
            for i in range(1,num):
                if num % i != 0:
                    count = count + 1
            if count == num - 2:
                print "%d是质数" % num

    def twentyTwo(self):
        '''
        九九乘法表
        笔记：输出不回车，加个 ','即可
        :return:
        '''
        num = range(1,10)
        for y in num:
            for x in range  (1, y + 1):
                print "%d * %d = %d" % (x, y, x * y),
            print "\n"

if __name__ == '__main__':
    Chen().one()
    # Chen().eight()
    # Chen().ten()    #有问题，没写完
    # Chen().twelve()
    # Chen().twentyOne()
    # Chen().twentyTwo()
