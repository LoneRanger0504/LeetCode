"""
给定一个二进制数组， 计算其中最大连续1的个数。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        遇1,count加1，判断是否大于最大值
        遇0，count置0，重新计数
        """
        count = 0
        max = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0
                continue
        return max


if __name__ == '__main__':
    input_list = [1, 1, 0, 1, 1, 1]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(input_list)
    print(result)
