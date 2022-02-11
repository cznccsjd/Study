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

    # 思路：遍历string,放到到一个新字符串中，每当由重复字符时：1、记录下当前不重复的长度；2、去掉重复字符及其之前的字符；3、继续遍历；
    # 但是，有个Bug，" "这个结果是0，应该是1
    def length_of_longest_substring_220210(self, s):
        new_str = ''   #加个默认的空格，因为传入的字符串也有可能只是个空格
        long = [0]      #加个默认值0，防止传进来的是""

        for i in range(len(s)):
            if s[i] not in new_str:
                new_str += s[i]
            else:
                cur_long = len(new_str)  # 记录有重复字符时，当前无重复字符串的长度
                long.append(cur_long)
                print(f"此时长度为{cur_long}的无重复字符串为{new_str}")
                new_strs = new_str.split(s[i])  # 去掉从开始到重复字符
                new_str = new_strs[1] + s[i]  # 别忘了新的字符串要再最后把这个重复字符串加回去



            # if i not in new_str and i == ' ':
            #     new_str += "\n"
            # elif i not in new_str:
            #     new_str += i
            # else:
            #     cur_long = len(new_str)     #记录有重复字符时，当前无重复字符串的长度
            #     long.append(cur_long)
            #     print(f"此时长度为{cur_long}的无重复字符串为{new_str}")
            #     new_strs = new_str.split(i)     #去掉从开始到重复字符
            #     new_str = new_strs[1] + i       #别忘了新的字符串要再最后把这个重复字符串加回去
        return max(long)


if __name__ == '__main__':
    so = Solution()
    s = "asdfghjkdl;kjhgftryuiooiuytw   poiyuytyteyutuyui"
    print(so.length_of_longest_substring_01(s))
    print(so.length_of_longest_substring_220210(s))
