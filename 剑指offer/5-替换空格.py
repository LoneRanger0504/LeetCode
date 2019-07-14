# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        # replace函数
        # return s.replace(' ', '%20')
        if not s:
            return ''
        count = 0
        for i in s:
            if i == ' ':
                count += 1
        res = list(s) + [0] * (2 * count)
        pointer1 = len(s) - 1
        pointer2 = len(res) - 1
        while pointer1 >= 0:
            if res[pointer1] != ' ':
                res[pointer2] = res[pointer1]
                pointer1 -= 1
                pointer2 -= 1
            else:
                res[pointer2 - 2] = '%'
                res[pointer2 - 1] = '2'
                res[pointer2] = '0'
                pointer1 -= 1
                pointer2 -= 3
        return ''.join(res)


if __name__ == '__main__':
    input_s = ' We are happy '
    solution = Solution()
    res = solution.replaceSpace(input_s)
    print(res)
