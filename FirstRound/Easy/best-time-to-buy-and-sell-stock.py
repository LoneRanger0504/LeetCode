"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        有两种情况返回0:一种是list为空；一种是第一个值是最大值（含等于情况）
        设置两个初始值，最小值与最大利润
        遍历一遍列表，找到最小值，对后续元素只需与最小值相减，差大于0保存为最大利润，否则就返回0
        """
        if len(prices) == 0:
            return 0
        min_value = 2 ** 31
        max_profit = 0
        for i in prices:
            if i < min_value:
                min_value = i
            if i - min_value > max_profit:
                max_profit = i - min_value
        return max_profit


if __name__ == '__main__':
    input_list = [1, 2]
    solution = Solution()
    result = solution.maxProfit(input_list)
    print(result)
