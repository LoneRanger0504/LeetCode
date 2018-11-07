class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 3:
            return -1
        left = nums[0]
        right = 0
        for i in range(nums_len - 1, 1, -1):
            right += nums[i]
        for i in range(0, nums_len - 1):
            if left != right:
                left = left + nums[i]
                right = right - nums[i + 1]
            else:
                return i
        return -1
