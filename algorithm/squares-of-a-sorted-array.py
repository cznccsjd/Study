#coding:utf-8
"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        zero = -1
        for i in range(n):
            if nums[i] < 0:
                zero = i

        list1 = []
        for i in range(zero+1):
            list1.append(nums[i] * nums[i])

        for i in range(zero+1, n):
            list1.append(nums[i] * nums[i])
        list1.sort()
        return list1

    def sortedSquares1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        zero = -1
        for i in range(n):
            if nums[i] < 0:
                zero = i

        ans = []
        i, j = zero, zero + 1
        while i >= 0  or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
            elif j == n:    #会陷入死循环
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1

        return ans

    def sortedSquares2(self, nums):
        n = len(nums)
        ans = [0] * n

        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        return ans

if __name__ == '__main__':
    list = [-7,-3,2,3,11]
    so = Solution()
    print(so.sortedSquares2(list))