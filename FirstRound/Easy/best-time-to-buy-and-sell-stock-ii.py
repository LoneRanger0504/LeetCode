"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        这里的最大利润其实就是所有非负利润的累加，只需要判断后一天减去前一天是否有利润，累加即可
        """
        prices_len = len(prices)
        if prices_len == 0:
            return 0

        max_profit = 0
        for i in range(prices_len - 1):
            if prices[i + 1] - prices[i] > 0:
                max_profit += prices[i + 1] - prices[i]

        return max_profit
    

if __name__ == '__main__':
    input_list = [4, 2, 3, 4, 2, 5]
    solution = Solution()
    result = solution.maxProfit(input_list)
    print(result)
