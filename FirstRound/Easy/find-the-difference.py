"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
"""


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        """
        1.用一个HashMap存储s中元素出现次数，再扫描t，不在keys()中或者出现次数大于values值
        2.异或，将s和t拼接起来一次遍历，异或最后得到的值就是多出来的不同元素
        ord()将字符转换成ASCII码，chr()将ASICC码转为字符
        """
        dic = {}
        for i in s:
            dic[i] = s.count(i)
        for i in t:
            if i not in dic.keys() or t.count(i) > dic.get(i):
                return i

        # ch = 0
        # for i in s + t:
        #     ch ^= ord(i)
        # return chr(ch)


if __name__ == '__main__':
    input_s = "abcd"
    input_t = "abcde"
    solution = Solution()
    res = solution.findTheDifference(input_s, input_t)
