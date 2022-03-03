#coding:utf-8
"""
选择排序
选择排序是给每个位置选择当前元素最小的，比如给第一个位置选择最小的，在剩余元素里面给>二个元素选择第二小的，依次类推，直到第n-1个元素，第n个 元素不用选择了，因为只剩下它一个最大的元素了。

那么，在一趟选择，如果当前元素比一个元素小，而该小的元素又出现在一个和当前元素相等的元素后面，那么 交换后稳定性就被破坏了。

比较拗口，举个例子，序列5 8 5 2 9， 我们知道第一遍选择第1个元素5会和2交换，那么原序列中2个5的相对前后顺序就被破坏了，所以选择排序不是一个稳定的排序算法。

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
以此类推，直到所有元素均排序完毕
时间负复杂度：O(n^2)，空间O（1），非稳定排序，原地排序
"""
def selection_sort(list):
    # python针对list，自带了个sort()方法，可以排序；
    # list.sort()
    # return list

    n = len(list)
    for i in range(n-1):
        flag = False
        for j in range(i,n-1):
            if list[i] > list[j+1]:
                flag = True
                tmp = list[j+1]
                list[j+1] = list[i]
                list[i] = tmp
        if not flag:
            break

    return list

test_list = [5,8,5,2,9]
test1 = selection_sort(test_list)
print(test1)