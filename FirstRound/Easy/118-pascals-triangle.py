# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        思路类似于120题，下一行的值等于上一行与它相邻的值的和
        直接初始化一个全1的二维三角矩阵，从第三行开始，迭代计算每个中间位置的值
        """
        if numRows < 0:
            return
        res = [[1 for j in range(i)] for i in range(1, numRows + 1)]
        if numRows >= 3:
            for i in range(2, len(res)):
                for j in range(1, i):
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


if __name__ == '__main__':
    input_numrows = 5
    solution = Solution()
    res = solution.generate(input_numrows)
    print(res)
