#coding:utf-8

# 九九乘法表
'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
1*4=4 2*4=8 3*4=12 4*4=16
...
1*9=9 2*9=18 3*9=27 ... 9*9=81
'''


for first_num in range(1,10):
    for second_num in range(1,first_num+1):
        print("%d*%d=%d" %(second_num,first_num,second_num*first_num))
    print("\n")