# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        先将数组排序依次，得到正确的元素顺序，初始化start， end
        再使用两次遍历，第一次正向遍历找到第一个不相等的数字，更新start，记作开始位置
        第二次反向遍历，还是寻找第一个不相等的数字，更新end，记作结束位置
        最后再判断一下start 和 end是不是没有变化，如果没变，表示数组已经是有序的，所求子数组长度为0
        否则返回 end - start + 1
        """
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        start = end = 0
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
        for j in range(len(nums) - 1, 0, -1):
            if nums[j] != sorted_nums[j]:
                end = j
                break
        if start == 0 and end == 0:
            return 0
        return end - start + 1


if __name__ == '__main__':
    input_nums = [2, 6, 4, 8, 10, 9, 15]
    solution = Solution()
    res = solution.findUnsortedSubarray(input_nums)
    print(res)
