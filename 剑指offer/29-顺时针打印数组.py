"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here

        def print_elements(matrix, rows, cols, start):
            X = cols - 1 - start
            Y = rows - 1 - start
            # 从左到右打印当前待打印矩阵局部的第一行
            for i in range(start, X + 1):
                res.append(matrix[start][i])
            # 判断是否需要打印一列
            if start < Y:
                for i in range(start + 1, Y + 1):
                    res.append(matrix[i][X])
            # 判断是否需要从右到左打印一行:
            if start < X and start < Y:
                for i in range(X - 1, start, -1):
                    res.append(matrix[Y][i])
            # 打印一列：
            if start < X and start < Y:
                for i in range(Y, start, -1):
                    res.append(matrix[i][start])

        if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        res = []
        while rows > start * 2 and cols > start * 2:
            print_elements(matrix, rows, cols, start)
            start += 1
        return res


if __name__ == '__main__':
    input_matrix = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                    ]
    solution = Solution()
    res = solution.printMatrix(input_matrix)
    print(res)