# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows = len(array) - 1
        cols = len(array[0]) - 1
        m = 0
        n = cols
        while m <= rows and n >= 0:
            if target == array[m][n]:
                return True
            elif target > array[m][n]:
                m += 1
            elif target < array[m][n]:
                n -= 1
        return False


if __name__ == '__main__':
    input_target = 4
    input_array = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    solution = Solution()
    res = solution.Find(input_target, input_array)
