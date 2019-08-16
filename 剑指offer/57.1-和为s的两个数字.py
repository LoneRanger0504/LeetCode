"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        start = 0
        end = len(array) - 1
        while start < end:
            sum = array[start] + array[end]
            if sum == tsum:
                return [array[start], array[end]]

            elif sum > tsum:
                end -= 1
            else:
                start += 1
        return []


if __name__ == '__main__':
    input_array = [1, 3, 5, 6, 7, 9]
    input_tsum = 8
    solution = Solution()
    res = solution.FindNumbersWithSum(input_array, input_tsum)
    print(res)