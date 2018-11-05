"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
"""


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        为什么这里最大子序和就是偶数位数字呢？
        """
        nums.sort()
        nums_len = len(nums)
        res = 0
        for i in range(nums_len):
            if i % 2 == 0:
                res += nums[i]
        return res


if __name__ == '__main__':
    input_arr = [1, 1]
    solution = Solution()
    result = solution.arrayPairSum(input_arr)
    print(result)
