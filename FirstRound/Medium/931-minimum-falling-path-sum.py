"""
给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。

下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。

"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        """
        动态规划，最关键的信息在于，在下一行选择的元素和当前行所选元素最多相隔一列
        因此状态转移方程分三种情况：
        (1)最左边一列，只能取上一行的同一列和后一列相加最小值，再加上当前位置值
        (2)最右边一列，只能取上一行的同一列和前一列相加的最小值，再加上当前位置值
        (3)其他情况，取上一行的同一列，前一列，后一列相加的最小值，再加上当前位置值
        """
        if not A:
            return 0
        rows = len(A)
        cols = len(A[0])
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    A[i][j] = min(A[i - 1][j], A[i - 1][j + 1]) + A[i][j]
                elif j == cols - 1:
                    A[i][j] = min(A[i - 1][j - 1], A[i - 1][j]) + A[i][j]
                else:
                    A[i][j] = min(A[i - 1][j - 1], A[i - 1][j], A[i - 1][j + 1]) + A[i][j]
        return min(A[-1][:])


if __name__ == '__main__':
    input_A = [[8, 93, 21], [18, -11, 19], [-23, 15, -42]]
    solution = Solution()
    res = solution.minFallingPathSum(input_A)
    print(res)
