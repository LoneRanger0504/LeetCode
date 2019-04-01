# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        使用HashMap减少时间复杂度，判断依据为num与difference都在HashMap的键中，且对应的index不相等
        又可以分为一遍Hash和两遍Hash
        """
        # 两遍Hash
        dic = {}
        res = [0] * 2
        for index in range(len(nums)):
            dic[nums[index]] = index
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dic.keys() and dic.get(difference) != i:
                res[0] = i
                res[1] = dic.get(difference)
                return res

        # 一遍Hash
        # dic = {}
        # for index, num in enumerate(nums):
        #     difference = target - num
        #     if difference in dic.keys() and index != dic.get(difference):
        #         return [dic.get(difference), index]
        #     dic[num] = index


if __name__ == '__main__':
    input_list = [2, 7, 11, 13]
    target = 9
    solution = Solution()
    res = solution.twoSum(input_list, target)
    print(res)
