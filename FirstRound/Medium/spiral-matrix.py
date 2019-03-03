"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        
        """

        def Print(matrix, cols, rows, start):
            endX = cols - 1 - start
            endY = rows - 1 - start
            # 从左向右添加到res，起始位置在matrix[start][start]，终止位置在matrix[start][endX]
            for i in range(start, endX + 1):
                res.append(matrix[start][i])
            # 从matrix[start][endX]开始向下添加，行数增加，终止位置在matrix[endY][endX]
            if start < endY:
                for i in range(start + 1, endY + 1):
                    res.append(matrix[i][endX])
            # 从右下角位置向左打印，endX--，终止位置在matrix[endY][start]
            if start < endX and start < endY:
                for i in range(endX - 1, start, -1):
                    res.append(matrix[endY][i])
            # 从左下角位置向上打印，endY--
            if start < endX and start < endY:
                for i in range(endY, start, -1):
                    res.append(matrix[i][start])

        res = []
        if len(matrix) <= 0:
            return res
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        # 当行数和列数大于2倍的当前左上角索引时继续循环
        while cols > start * 2 and rows > start * 2:
            Print(matrix, cols, rows, start)
            start += 1
        return res


if __name__ == '__main__':
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    res = solution.spiralOrder(input_matrix)
    print(res)
