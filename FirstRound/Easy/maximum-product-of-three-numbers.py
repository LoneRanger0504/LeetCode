"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
"""


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        将数组排序，考虑最大乘积会受负数影响，当最大值小于0或最小值大于0时，最大乘积就是排序后的最后三项
        当有正有负时，最大值也只有两种情况，最小的两个负数相乘再乘以最后一个数；最后三个数相乘
        但是可以再简化一些，提出公共的乘子
        """
        nums_len = len(nums)
        nums.sort()
        if nums_len == 3 or nums[0] > 0 or nums[-1] < 0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            value_1 = nums[-1] * nums[-2] * nums[-3]
            value_2 = nums[0] * nums[1] * nums[-1]
            return value_1 if value_1 > value_2 else value_2


if __name__ == '__main__':
    input_list = [-1, 3, 43, -2, 6]
    solution = Solution()
    result = solution.maximumProduct(input_list)
    print(result)
