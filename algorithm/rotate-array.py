#coding:utf-8
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = k % n

        new_list = [0] * n
        for i in range(n):
            if i + k <= n - 1:
                new_list[i+k] = nums[i]
            else:
                new_list[i+m-n] = nums[i]

        return new_list

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 30
    so = Solution()
    print(so.rotate(nums, k))