# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        其实原理和斐波那契一样，都是由前两个值来决定当前值，只不过当前值的更新并不是前两个值相加
        而是取前两个值中的较小值与当前值相加，这样当前值就也是最小cost，
        状态转移方程：dp[i] = min(dp[i-2], dp[i-1]) + dp[i]
        最后能够达到顶层，取最后两个位置中的较小值，就是整体的最小cost
        """
        if not cost or len(cost) < 2:
            return
        min_cost = [0] * len(cost)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]
        for i in range(2, len(min_cost)):
            min_cost[i] = min(min_cost[i - 2], min_cost[i - 1]) + cost[i]
        return min(min_cost[-1], min_cost[-2])


if __name__ == '__main__':
    input_cost = [10, 15, 20]
    solution = Solution()
    res = solution.minCostClimbingStairs(input_cost)
    print(res)
