"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        (1)O(N)解法：双指针，只固定一个指针i，j则根据具体情况滑动。
        当子数组和小于s时，j++，sum += nums[j]
        当子数组和大于等于s之后，记录当前子数组长度，取较小值，
        然后再将位置i上的元素从子数组删除，也就是指针i向右走一位，循环直到i指针到达数组末尾
        (2)
        """
        i, j = 0, 0
        sum = 0
        res = float('inf')
        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                res = min(res, j - i)
            sum -= nums[i]
        return res if res != float('inf') else 0


if __name__ == '__main__':
    input_s = 7
    input_nums = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    res = solution.minSubArrayLen(input_s, input_nums)
    print(res)
