"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        依次遍历，将不等于0的数按顺序交换至列表前部
        """
        nums_len = len(nums)
        index = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1


if __name__ == '__main__':
    input_list = [1, 8, 0, 4, 0, 4, 0, 7, 0]
    solution = Solution()
    result = solution.moveZeroes(input_list)
