"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        先算出前K个数的和，保存最初值
        遍历列表，每次计算不用重新加K个值，只需要将最初值减去第i个值再加上第i+k个值
        与最初值比较，保存最大值，返回最大值除以k即可
        """
        nums_len = len(nums)
        sum = 0
        for i in range(k):
            sum += nums[i]
        max = sum
        for i in range(nums_len - k):
            sum = sum - nums[i] + nums[i + k]
            if sum > max:
                max = sum
        return max / k


if __name__ == '__main__':
    input_list = [1, 12, -5, -6, 50, 3]
    input_k = int(input())
    solution = Solution()
    result = solution.findMaxAverage(input_list, input_k)
    print(result)
