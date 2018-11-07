"""
给定一个未经排序的整数数组，找到最长且连续的的递增序列。
"""


class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        很简单的思路，就是使用一个count计数，递增就加1，否则置1，最终返回max与count的较大值
        """
        count = 1
        max = 0
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        for i in range(nums_len - 1):
            if nums[i] < nums[i + 1]:
                count += 1
                if count > max:
                    max = count
            else:
                count = 1
                continue
        return max if max > count else count


if __name__ == '__main__':
    input_list = [1, 2, 3, 2]
    solution = Solution()
    result = solution.findLengthOfLCIS(input_list)
    print(result)
