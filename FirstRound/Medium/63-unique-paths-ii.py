# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        还是比较直接的动态规划，参照62题，状态转移方程其实还是原来的，只不过加上了关于障碍的判断
        并且在最开始构造的时候，赋值边界位置的时候，一旦输入的obstacleGrid对应位置上为1表示有障碍，该位置后面的都不用再更新，因为到达不了该位置了
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for i in range(n)] for j in range(m)]
        #  处理第一列，如果输入矩阵中对应位置上有障碍，结束循环，否则将边界置为1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            matrix[i][0] = 1
        #  处理第一行，原理同上
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            matrix[0][i] = 1
        #  从matrix[1][1]开始，如果输入矩阵对应位置为1，则matrix对应位置为0，否则就按照状态转移方程更新
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                else:
                    continue
        return matrix[m - 1][n - 1]


if __name__ == '__main__':
    input_obstacleGrid = [[1, 0]]
    solution = Solution()
    res = solution.uniquePathsWithObstacles(input_obstacleGrid)
    print(res)
