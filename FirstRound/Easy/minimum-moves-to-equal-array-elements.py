"""
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
"""


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        每次让n-1个元素加1，其实可以理解为依次把最大的数减1，直到所有的数都为最小值
        遍历统计每个数与最小值的差累加就是最小移动次数
        还有一种方式是将数组的和减去最小值乘以数组长度，原理和上述类似
        return sum(nums) - len(nums)*min(nums)
        """
        min_value = min(nums)
        count = 0
        for num in nums:
            if num != min_value:
                count += (num - min_value)
        return count


if __name__ == '__main__':
    input_list = [1, 2, 3]
    solution = Solution()
    res = solution.minMoves(input_list)
