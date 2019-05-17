# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)
给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
"""


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        """
        原理基本同303，这里还是先用一个二维数组来存储每行的每个位置的累加值
        后面计算某个子矩阵的和的时候只需要对对应的行数执行相应次数的一维数组求范围和即可
        """
        if not matrix:
            return
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = matrix
        for i in range(self.rows):
            sum = 0
            for j in range(self.cols):
                sum += matrix[i][j]
                self.matrix[i][j] = sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        """
        首先需要加以判断输入的值是否有效
        后面的求和其实就简化为(row2-row1)次的一维数组求范围和，原理同303
        """
        if row1 < 0 or col1 < 0 or row2 > self.rows or col2 > self.cols:
            return
        sum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                sum += self.matrix[i][col2]
            else:
                sum += self.matrix[i][col2] - self.matrix[i][col1 - 1]
        return sum
