"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        根据矩阵的特点，每行递增，前一行的最大一个数小于后一行的最小一个数
        从右上角开始遍历查找，找到直接返回，
        没找到判断与target的关系，小于目标值表示在后面的行，行数加1
        大于目标值表示在前面的列，列数减1
        循环结束的条件是到达行和列的边界
        """
        if not matrix:
            return False
        M = 0
        N = len(matrix[0]) - 1
        while M <= len(matrix) - 1 and N >= 0:
            if matrix[M][N] == target:
                return True
            if matrix[M][N] > target:
                N -= 1
            if matrix[M][N] < target:
                M += 1
        return False


if __name__ == '__main__':
    input_matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    input_target = 3
    solution = Solution()
    res = solution.searchMatrix(input_matrix, input_target)
