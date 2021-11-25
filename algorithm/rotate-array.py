#coding:utf-8
"""
双指针：
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""

class Solution:
    # 自己想的实现方式，但是没有用双指针
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

    def rotate1(self, nums, k):
        """
        环状替换
        """
        n = len(nums)
        k = k % n
        count = self.gcd(n, k)

        for start in range(count):
            current = start
            sign = True
            next = (current + k) % n
            pres = nums[current]

            while(sign):
                temp = nums[next]
                nums[next] = pres
                pres = temp
                current = next
                next = (current + k) % n
                if next == start:
                    nums[next] = pres
                    sign = False
        return nums

    # 获取最大公约数
    def gcd(self, x, y):
        # return y > 0 ? gcd(y, x%y): x
        if y > 0:
            return self.gcd(y, x % y)
        else:
            return x

    def rotate3(self, nums, k):
        """
        直接根据k截断数组，把后面的数组移动到前面去
        """
        n = len(nums)
        k = k % n
        return nums[n-k:] + nums[:n-k]

    def rotate4(self, nums, k):
        """
        翻转数组
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        nums1 = nums[:k]
        nums2 = nums[k:]
        nums1.reverse()
        nums2.reverse()
        return nums1 + nums2

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    so = Solution()
    print(so.rotate4(nums, k))