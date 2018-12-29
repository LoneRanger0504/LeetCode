"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        先对比两个字符串构成的set长度是否相等，这里已经包括了存在重复元素的情况
        使用一个字典，以s[i]为key，t[i]为value，每次添加的时候进行判断
        如果key不存在，添加键和值；如果key已经存在，判断对应的value与t[i]是否相等，不相等则返回FALSE
        最后返回TRUE
        """
        if len(set(s)) != len(set(t)):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic.keys():
                if dic.get(s[i]) != t[i]:
                    return False
            else:
                dic[s[i]] = t[i]
        return True


if __name__ == '__main__':
    input_s = 'egg'
    input_t = 'abb'
    solution = Solution()
    res = solution.isIsomorphic(input_s, input_t)
