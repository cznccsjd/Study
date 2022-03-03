#coding:utf-8

"""
学习冒泡排序
"""

def bubble_sort_v1(list):
    """最简单的实现，时间复杂度 o(n^2)，空间 o 1，原地算法，稳定"""
    n = len(list)

    num = 0

    # for i in range(n):
    for i in range(n-1):    #i=0时，只需要循环n-1次即可，因为当i=n-1时，n-i-1=n-(n-1)-1=0,j in range(0)一定无法循环;当i=n-2时，n-i-1=n-(n-2)-1=1,j in range(1)还可以循环1次
        for j in range(n-i-1):
            num += 1
            if list[j] > list[j+1]:
                tmp = list[j+1]
                list[j+1] = list[j]
                list[j] = tmp

    print(f'最终循环了{num}次')
    return list

def bubble_sort_v2(list):
    n = len(list)

    num = 0

    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            num += 1
            if list[j+1] < list[j]:
                flag = True
                tmp = list[j+1]
                list[j+1] = list[j]
                list[j] = tmp

        if not flag:
            break
    print(f'最终循环了{num}次')
    return list

test_list = [5,6,2,3,4,1,7,8,9]
# test1 = bubble_sort_v1(test_list)
# print(test1)

test2 = bubble_sort_v2(test_list)
print(test2)