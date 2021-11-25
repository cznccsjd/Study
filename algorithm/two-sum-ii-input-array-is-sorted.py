#coding:utf-8
"""
两数之和-输入有序数组
给定一个已按照 非递减顺序排列 的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        暴力计算，没有利用到有序数组条件
        """
        n = len(numbers)
        for left in range(n):
            for right in range(left+1, n):
                if target == numbers[left] + numbers[right]:
                    return [left + 1, right + 1]

    def twoSum2(self, numbers, target):
        """
        二分查找
        先遍历第一个数，时间复杂度：O(n)
        二分查找第二个数，时间复杂度O(log n)
        最终时间复杂度 O(n log n)
        空间复杂度O(1)
        """
        n = len(numbers)
        right = n - 1
        for start in range(n):
            left = start
            while(left <= right):
                middle = left + (right - left) // 2
                if target == numbers[start] + numbers[middle]:
                    return [start + 1, middle + 1]
                elif target < numbers[start] + numbers[right]:
                    right = middle - 1
                else:
                    left = middle + 1

    def twoSum3(self, numbers, target):
        """
        双指针
        """
        n = len(numbers)
        left , right = 0, n - 1
        while(left <= right):
            if target == numbers[left] + numbers[right]:
                return [left + 1, right + 1]
            elif target > numbers[left] + numbers[right]:
                left += 1
            else:
                right -= 1      #这里如果用二分查找法，right定位的会更快点

if __name__ == '__main__':
    numbers = [2,3,4]
    target = 6
    so = Solution()
    print(so.twoSum3(numbers, target))