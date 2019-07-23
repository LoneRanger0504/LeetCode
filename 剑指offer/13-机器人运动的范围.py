# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def getDigitNum(number):
            sum = 0
            while number > 0:
                sum += number % 10
                number //= 10
            return sum

        def canMove(row, col):
            if 0 <= row < rows and \
                    0 <= col < cols and \
                    getDigitNum(row) + getDigitNum(col) <= threshold and \
                    visited[row * cols + col] == 0:
                return True
            return False

        def movingCountCore(row, col):
            count = 0
            if canMove(row, col):
                visited[row * cols + col] = 1
                count = 1 + movingCountCore(row + 1, col) \
                        + movingCountCore(row - 1, col) \
                        + movingCountCore(row, col + 1) \
                        + movingCountCore(row, col - 1)
            return count

        if threshold < 0 or rows < 1 or cols < 1:
            return False
        visited = [0] * (rows * cols)
        count = movingCountCore(0, 0)
        return count


if __name__ == '__main__':
    input_threshold = 5
    input_rows = 10
    input_cols = 10
    solution = Solution()
    res = solution.movingCount(input_threshold, input_rows, input_cols)
    print(res)
