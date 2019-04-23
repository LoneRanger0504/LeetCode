# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        思路类似于矩阵的最小路径和，先确定状态转移方程，triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        当前位置的最小路径和只与上一层中与他相邻的节点有关，与他相邻的条件是列索引减1或者不变
        首先把三角形外侧的两边的元素值确定，类似于矩阵路径中的确定第一行和第一列
        这里再从第三行开始，根据状态转移方程更新每个位置的最小路径和，返回最后一行的最小值
        """
        if not triangle:
            return 0
        m = len(triangle)
        #  更新三角形的左侧边
        for i in range(1, m):
            triangle[i][0] = triangle[i - 1][0] + triangle[i][0]
        #  更新三角形的右侧边
        for i in range(1, m):
            triangle[i][i] = triangle[i - 1][i - 1] + triangle[i][i]
        #  从第三行开始，才会有两个相邻的值，因为前边算过了左右两侧的边，这里j的范围是[1-(i-1)]
        for i in range(2, m):
            for j in range(1, i):
                triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        return min(triangle[m - 1])
