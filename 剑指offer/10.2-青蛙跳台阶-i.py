# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        dp = [0] * number
        dp[0] = 1
        dp[1] = 2
        for i in range(2, number):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number - 1]


if __name__ == '__main__':
    input_number = 4
    solution = Solution()
    res = solution.jumpFloor(input_number)
    print(res)
