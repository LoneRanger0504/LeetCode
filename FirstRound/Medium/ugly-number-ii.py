# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
编写一个程序，找出第 n 个丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        从1开始计算所有的丑数加到list中，每次更新list取对应的三指针的index分别乘2,3,5中的最小值
        """
        if n <= 0:
            return
        res = [0] * n
        res[0] = 1
        index2 = index3 = index5 = 0
        next_ugly_index = 1
        while next_ugly_index < n:
            min_ugly = min(res[index2] * 2, res[index3] * 3, res[index5] * 5)
            res[next_ugly_index] = min_ugly

            while res[index2] * 2 <= res[next_ugly_index]:
                index2 += 1
            while res[index3] * 3 <= res[next_ugly_index]:
                index3 += 1
            while res[index5] * 5 <= res[next_ugly_index]:
                index5 += 1
            next_ugly_index += 1

        ugly = res[n - 1]
        return ugly


if __name__ == '__main__':
    input_index = 11
    solution = Solution()
    res = solution.nthUglyNumber(input_index)
    print(res)
