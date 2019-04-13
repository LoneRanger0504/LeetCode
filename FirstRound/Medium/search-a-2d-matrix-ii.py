"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        思路同上一题，可以从左下或者右上开始找
        """
        if not matrix:
            return False
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        m = rows
        n = 0
        while m >= 0 and n <= cols:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                n += 1
            else:
                m -= 1
        return False


if __name__ == '__main__':
    input_matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    input_target = 5
    solution = Solution()
    res = solution.searchMatrix(input_matrix, input_target)
