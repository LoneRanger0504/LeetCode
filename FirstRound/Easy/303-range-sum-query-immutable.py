# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        """
        将数组进行简单处理，储存已经计算的结果，减少重复计算。
        这里是通过累加前面每个位置得到当前总和，后面求范围和的时候直接根据位置关系计算即可
        """
        if not nums:
            return
        self.list = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.list.append(sum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        """
        先判断i和j是否有效
        再稍微区分一下，如果i从0开始，则范围和直接为j位置处的值，因为前面已经累加过了
        如果i不是从0开始，范围和等于list[j]减去list[i-1]
        """
        if i < 0 or j > len(self.list):
            return

        if i == 0:
            res = self.list[j]
            return res
        else:
            res = self.list[j] - self.list[i - 1]
            return res


if __name__ == '__main__':
    obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    par = obj.sumRange(2, 5)
    print(par)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
