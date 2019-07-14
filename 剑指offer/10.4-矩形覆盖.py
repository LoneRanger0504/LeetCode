# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


class Solution:
    def rectCover(self, number):
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
    res = solution.rectCover(input_number)
    print(res)
