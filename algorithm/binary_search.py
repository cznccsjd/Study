#coding:utf-8
"""
二分查找
https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-by-leetcode/
"""
def search(nums, target):
    nums.sort(reverse=False)
    n = len(nums)
    left, right = 0, n-1

    while(left <= right):
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1


test_list = [1, 2, 3, 6, 8, 9, 12,23,89,102,111,123,149]
test_target = 1021
print(search(test_list, test_target))