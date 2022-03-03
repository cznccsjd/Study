#coding:utf-8

"""
归并排序
"""

def merge_sort(lists, start, end):
    mid = (start + end) // 2
    if start < end:
        # 拆成两个小集合，分别进行递归
        merge_sort(lists, start, mid)
        # merge_sort_core(lists, start, mid, end)
        merge_sort(lists, mid+1, end)
        # 把两个有序小集合，归并成一个大集合
        merge_sort_core(lists, start, mid, end)

def merge_sort_core(lists, start, mid, end):
    tmp_list = []
    p1 = start
    p2 = mid+1
    p = 0

    while(p1 <= mid and p2 <= end):
        if lists[p1] <= lists[p2]:
            tmp_list.append(lists[p1])
            p1 += 1
        else:
            tmp_list.append(lists[p2])
            p2 += 1
        p += 1

    while p1 <= mid:
        tmp_list.append(lists[p1])
        p1 += 1

    while p2 <= end:
        tmp_list.append(lists[p2])
        p2 += 1

    for i in range(len(tmp_list)):
        lists[i+start] = tmp_list[i]

test_list = [12,40,7,31,31,21,42,40,4,12,32,21,41,35,46]
merge_sort(test_list, 0, len(test_list)-1)
print(test_list)