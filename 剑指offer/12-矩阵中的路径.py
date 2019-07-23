# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        def hasPathCore(row, col, path_index):
            if path_index == len(path):
                return True
            hasPath = False
            if 0 <= row < rows and 0 <= col < cols and path[path_index] == matrix[row * cols + col] and visited[
                row * cols + col] != 1:
                path_index += 1
                visited[row * cols + col] = 1
                hasPath = hasPathCore(row + 1, col, path_index) \
                          or hasPathCore(row - 1, col, path_index) \
                          or hasPathCore(row, col + 1, path_index) \
                          or hasPathCore(row, col - 1, path_index)
                if not hasPath:
                    path_index -= 1
                    visited[row * cols + col] = 0
            return hasPath

        if not matrix or rows < 1 or cols < 1 or not path:
            return False
        visited = [0] * (rows * cols)
        path_index = 0
        for i in range(rows):
            for j in range(cols):
                if hasPathCore(i, j, path_index):
                    return True
        return False


if __name__ == '__main__':
    input_matrix = "ABCESFCSADEE"
    input_rows = 3
    input_cols = 4
    input_path = "ABCB"
    solution = Solution()
    res = solution.hasPath(input_matrix, input_rows, input_cols, input_path)
    print(res)
