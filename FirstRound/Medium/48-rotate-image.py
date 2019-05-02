"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        先沿着对角线交换对角线两侧的值，再对每一行倒序输出，其实就是再按照中轴线交换
        """
        if not matrix:
            return
        n = len(matrix)
        for i in range(n):
            #  只更新对角线下面的j
            for j in range(i):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        print(matrix)


if __name__ == '__main__':
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    res = solution.rotate(input_matrix)
