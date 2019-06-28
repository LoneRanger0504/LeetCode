# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        DP四要素：
        （1）状态：最后一步能够偷取的最大金额
        （2）状态转移方程： dp[i] = max(dp[i-1], dp[i-2]) + nums[i]
        （3）初始值，边界： dp[0] = nums[0]， 从第三个值到最后一个值
        （4）计算顺序：从左到右
        """
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])
        return max(res)


if __name__ == '__main__':
    input_nums = [2, 7, 9, 3, 1]
    solution = Solution()
    res = solution.rob(input_nums)
    print(res)
