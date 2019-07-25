# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        """
        :param array:
        :return:
        """
        """
        题目要求要保持奇数和偶数的顺序不变，即可以实现一种稳定排序，例如插入排序
        有一种更简单的方式，用空间换时间，从头遍历一遍，奇数偶数分开添加到两个数组，最后合并一下
        如果不要求稳定性，则使用双指针
        """
        if not array:
            return []

        def isOdd(num):
            if num & 1 != 0:
                return True
            else:
                return False

        odd = []
        even = []
        for i in array:
            if isOdd(i):
                odd.append(i)
            else:
                even.append(i)
        return odd + even
        # 2.双指针
        # if not array:
        #     return []
        #
        # def isOdd(num):
        #     if num & 1 != 0:
        #         return True
        #     else:
        #         return False
        # start = 0
        # end = len(array) - 1
        # while start < end:
        #     if start < end and isOdd(array[start]):
        #         start += 1
        #     if start < end and not isOdd(array[end]):
        #         end -= 1
        #     if start < end:
        #         array[start], array[end] = array[end], array[start]
        # return array


if __name__ == '__main__':
    input_array = [1, 23, 654, 2, 653, 242, 12, 845]
    solution = Solution()
    res = solution.reOrderArray(input_array)
    print(res)
