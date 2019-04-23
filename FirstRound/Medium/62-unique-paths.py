# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        还是动态规划，除了边缘的位置，其他位置上可能的路径数就是他的左位置和上位置的值相加
        即状态转移方程为 matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        初始化的时候直接全1初始化，从matrix[1][1]开始遍历非边缘位置，最后右下角的值就是所有的路径数之和
        有一种更直接的解法，其实是一个组合问题，求解C((m-1),(m+n-2))
        """
        matrix = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[m - 1][n - 1]


if __name__ == '__main__':
    input_m = 7
    input_n = 3
    solution = Solution()
    res = solution.uniquePaths(input_m, input_n)
    print(res)
