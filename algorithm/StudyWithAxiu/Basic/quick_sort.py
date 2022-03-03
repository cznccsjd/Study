#coding:utf-8

"""
快速排序
算法思想

1、选取第一个数为基准

2、将比基准小的数交换到前面，比基准大的数交换到后面

3、对左右区间重复第二步，直到各区间只有一个数

我们从数组中选择一个元素，我们把这个元素称之为中轴元素吧，然后把数组中所有小于中轴元素的元素放在其左边，所有大于或等于中轴元素的元素放在其右边，显然，此时中轴元素所处的位置的是有序的。也就是说，我们无需再移动中轴元素的位置。

从中轴元素那里开始把大的数组切割成两个小的数组(两个数组都不包含中轴元素)，接着我们通过递归的方式，让中轴元素左边的数组和右边的数组也重复同样的操作，直到数组的大小为1，此时每个元素都处于有序的位置。
"""
def quick_sort_axiu(arr, low, high):
    if low >= high:     # 结束条件
        return False;
    first = low
    last = high
    key = arr[first]    # 设置基准

    while first < last:
        # 从后往前走，将第一个比key小的数值，跟key对换位置
        while first < last and arr[last] > key:
            last -= 1
        if first < last:
            tmp = arr[first]
            arr[first] = arr[last]
            arr[last] = tmp

        # 从前往后走，将第一个比key大的数值，跟key对换位置
        while first < last and arr[first] <= key:
            first += 1
        if first < last:
            tmp = arr[first]
            arr[first] = arr[last]
            arr[last] = tmp

    arr[first] = key    # 这个好像没啥用
    # 前半递归
    quick_sort_axiu(arr, low, first-1)
    # 后半递归
    quick_sort_axiu(arr, first+1, high)

def quick_sort_define(lists):
    n = len(lists)
    quick_sort_axiu(lists, 0, n-1)

def quick_sort_jlz_main(lists):
    n = len(lists)
    quick_sort_jlz_detail(0, n-1, lists)

def quick_sort_jlz_detail(left, right, lists):
    if left >= right:
        return False

    first = left
    last = right
    key = lists[first]

    while first < last:
        while lists[last] > key:
            last -= 1
        if first < last:
            tmp = lists[first]
            lists[first] = lists[last]
            lists[last] = tmp

        while lists[first] <= key:
            first += 1
        if first < last:
            tmp = lists[first]
            lists[first] = lists[last]
            lists[last] = tmp

    quick_sort_jlz_detail(left, first-1, lists)
    quick_sort_jlz_detail(first+1, right, lists)

test_list = [13,44,38,5,47,4,15,36,2,19,48]
# quick_sort_define(test_list)
quick_sort_jlz_main(test_list)
print(test_list)
