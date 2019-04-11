# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :
"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        先判断特殊情况，num为非正数
        依次判断能否一直被2,3,5整除直到等于1
        """
        if num <= 0:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5

        return num == 1


if __name__ == '__main__':
    input_num = 6
    solution = Solution()
    res = solution.isUgly(input_num)
    print(res)
