/*
双指针：
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 */
package Algorithm;

import java.util.Arrays;

public class RotateArray {
    public int[] rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        int count = gcd(k, n);
        for (int start = 0; start < count; ++start) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % n;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
            }while (start != current);
        }
        return nums;
    }

//    计算最大公约数,eg：[6,2]=2
    public int gcd(int x, int y) {
        return y > 0 ? gcd(y, x % y) : x;
    }

    public static void main(String[] args) {
        int nums[] = {1,2,3,4,5,6};
        int k = 2;
        RotateArray test = new RotateArray();
        System.out.println(Arrays.toString(test.rotate(nums, k)));
    }
}
