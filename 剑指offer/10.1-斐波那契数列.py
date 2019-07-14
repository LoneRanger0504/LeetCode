# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""


class Solution:
    def Fibonacci(self, n):
        # write code here
        dp = [1] * n
        if n < 0:
            return
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return dp[n - 1]
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]


if __name__ == '__main__':
    input_n = 0
    solution = Solution()
    res = solution.Fibonacci(input_n)
    print(res)
