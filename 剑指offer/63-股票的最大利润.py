"""
假设某只股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些时间节点的价格为[9, 11, 8, 5, 7, 12, 16, 14]如果我们能在价格为5的时候买入并在价格为16的时候卖出，则能获得最大利润为11
"""


class Solution:
    def maxProfit(self, nums):
        if not nums or len(nums) < 2:
            return 0
        min_price = nums[0]
        max_profit = nums[1] - min_price
        for i in range(2, len(nums)):
            if nums[i-1] < min_price:
                min_price = nums[i-1]
            cur_profit = nums[i] - min_price
            if cur_profit > max_profit:
                max_profit = cur_profit
        return max_profit




if __name__ == '__main__':
    input_prices = [9, 11, 8, 5, 7, 12, 16, 14]
    solution = Solution()
    res = solution.maxProfit(input_prices)
    print(res)