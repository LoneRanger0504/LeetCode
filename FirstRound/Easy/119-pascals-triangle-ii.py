# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        这里的解法其实和118一样，都是输入一个数字k生成相应的k行杨辉三角，取最后一行。
        常数级别的解法就是使用两个for循环，除了第一个数为1之外，后面的数都是上一次循环的数值加上它前面位置的数值之和，不停地更新每一个位置的值，便可以得到第n行的数字
        """
        if rowIndex < 0 or rowIndex > 33:
            return
        res = [[1 for j in range(i)] for i in range(1, rowIndex + 2)]
        if rowIndex >= 2:
            for i in range(1, len(res)):
                for j in range(1, i):
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[-1]


if __name__ == '__main__':
    input_rowIndex = 3
    solution = Solution()
    res = solution.getRow(input_rowIndex)
    print(res)
