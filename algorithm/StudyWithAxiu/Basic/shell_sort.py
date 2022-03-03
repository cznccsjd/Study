#coding:utf-8

"""
希尔排序可以说是插入排序的一种变种。无论是插入排序还是冒泡排序，如果数组的最大值刚好是在第一位，要将它挪到正确的位置就需要 n - 1 次移动。也就是说，原数组的一个元素如果距离它正确的位置很远的话，则需要与相邻元素交换很多次才能到达正确的位置，这样是相对比较花时间了。

希尔排序就是为了加快速度简单地改进了插入排序，交换不相邻的元素以对数组的局部进行排序。

希尔排序的思想是采用插入排序的方法，先让数组中任意间隔为 h 的元素有序，刚开始 h 的大小可以是 h = n / 2,接着让 h = n / 4，让 h 一直缩小，当 h = 1 时，也就是此时数组中任意间隔为1的元素有序，此时的数组就是有序的了。
"""
def shell_sort(nums):
    n = len(nums)
    # 进行分组，最开始的时候，gap为数组长度的一半
    gap = n // 2
    while (gap >= 1):
        for i in range(gap, n):
            inserted = nums[i]
            j = i - gap    # 引入j，是因为有可能某次循环中，nums[i-gap] < num[i-gap-gap]，这里跟插入排序是一样的
            while inserted < nums[j] and j >= 0:
                tmp = nums[j+gap]
                nums[j+gap] = nums[j]
                nums[j] = tmp
                j -= gap
            nums[j+gap] = inserted
        gap = gap // 2

test_lists = [5,7,8,3,91,22,4,6,12,66,19,88,1,21,74,9,34]    # 这个就有Bug
shell_sort(test_lists)
print(test_lists)