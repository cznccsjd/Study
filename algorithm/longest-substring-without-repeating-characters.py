#coding:utf-8
"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0


提示：

0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
        hahahah，自己的思路歪了，没做出来
        '''
        start = long = index = 0
        new_s = ''
        n = 0

        for i in s[index:]:
            n += 1
            if(i not in new_s):
                new_s += i
                start += 1
            else:
                # 1、找到这个重复的字符；2、找到这个重复字符在已遍历过的字符串中，上一次出现的位置；3、从这个字符上一次出现位置+1开始，继续遍历；
                tmp_index = s[:start].rfind(i)
                index = tmp_index + 1
                start = 0
                continue
            while(start > long):
                long = start
        print(f'无重复字符串为:{s[n - long:n]}')
        return long

    def length_of_longest_substring_01(self, s):
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为-1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 做指针向右以动一格，移除一个字符
                occ.remove(s[i - 1])
            # 不断移动右指针
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            # 第i到rk个字符是一个极长的无重复字符串字串
            ans = max(ans, rk - i + 1)
        return ans

if __name__ == '__main__':
    so = Solution()
    s = "asdfghjdqwehrtyuiopmnbvcxrthj"
    # print(so.lengthOfLongestSubstring(s))
    print(so.length_of_longest_substring_01(s))
