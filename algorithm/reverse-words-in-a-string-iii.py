#coding:utf-8
"""
反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def reverseWords(self, s):
        s_list = s.split(' ')
        new_s = ""
        for word in s_list:
            new_word = ""
            n_word = len(word)
            for i in range(n_word):
                new_word = word[i] + new_word
            new_s = new_s + new_word + ' '
        new_s.strip()       #有Bug，最右边的空格没有去掉，可以参考java文件：Study\StudyJava\src\Algorithm\ReverseWordsInAStringIII.java
        return new_s

if __name__ == '__main__':
    so = Solution()
    str = "Let's take LeetCode contest"
    print(str)
    print(so.reverseWords(str))