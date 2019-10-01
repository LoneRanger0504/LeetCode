"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        1.找到旋转位置，使用Python切片，注意如果要修改原数组的引用位置，需要使用nums[:]
        # nums[:] = nums[-k:] + nums[:-k]
        2.三次翻转，先翻转整个数组，再依次翻转前后两个部分
        """
        if not nums or len(nums) == 1:
            return nums
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution = Solution()
    solution.rotate(nums, 3)
