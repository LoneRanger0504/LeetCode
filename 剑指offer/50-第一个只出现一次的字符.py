# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        dic = {}
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic.get(i) + 1
        res = float('inf')
        for i in dic.keys():
            if dic.get(i) == 1:
                if s.index(i) < res:
                    res = s.index(i)
        return res


if __name__ == '__main__':
    input_s = 'fadjkgfkjdsfhdjskf'
    solution = Solution()
    res = solution.FirstNotRepeatingChar(input_s)
    print(res)
