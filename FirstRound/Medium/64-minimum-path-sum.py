# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        动态规划题，要找最后一个位置的最小路径，其实只和他的上方和左方位置有关，再依次倒退，上方的元素只和他的上方和左方元素有关
        但是其实我们求的时候，可以把之前的结果都缓存下来，在原数组的对应位置上更新达到该位置的最小路径和
        先考虑边界情况，先把第一行和第一列更新完，剩下的位置就可以根据状态方程grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]更新
        最后的右下角位置就是所有路径的最小路径和
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        #   更新第一列
        for i in range(m - 1):
            grid[i + 1][0] = grid[i][0] + grid[i + 1][0]
        #  更新第一行
        for j in range(n - 1):
            grid[0][j + 1] = grid[0][j] + grid[0][j + 1]
        #  更新剩余位置，只跟当前位置的上方位置和左方位置有关，取两者中的最小值加上当前位置的cost
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    input_grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    solution = Solution()
    res = solution.minPathSum(input_grid)
    print(res)
