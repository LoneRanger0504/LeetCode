# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        用二分查找依次找到第一个出现的索引和最后出现的索引，最后判断对应的index是否符合先后顺序
        需要注意的是在二分查找过程中要注意数组越界，注意检查下标是否有意义
        """

        def getFirstIndex(nums, start, end):
            if start > end:
                return -1
            mid = (start + end) / 2
            #  如果中间值等于target，再判断mid-1的值是否等于target，只有nums[mid-1]不等于target，mid才是正确的第一个索引，否则令end=mid-1继续递归查找，
            #  或者mid已经是0了，肯定是第一个index
            if nums[mid] == target:
                if (mid > 0 and nums[mid - 1] != target) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            return getFirstIndex(nums, start, end)

        def getLastIndex(nums, start, end):
            if start > end:
                return -1
            mid = (start + end) / 2
            #  这里判断类似查找第一个索引，需要判断nums[mid+1]是否为target，或者mid已经是最后一个索引
            if nums[mid] == target:
                if (mid < nums_len - 1 and nums[mid + 1] != target) or mid == nums_len - 1:
                    return mid
                else:
                    start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            return getLastIndex(nums, start, end)

        res = [-1, -1]
        if not nums:
            return res
        nums_len = len(nums)

        start = 0
        end = nums_len - 1

        first_index = getFirstIndex(nums, start, end)
        last_index = getLastIndex(nums, start, end)
        
        if first_index >= 0 and last_index <= len(nums) - 1:
            res[0] = first_index
            res[1] = last_index
        return res


if __name__ == '__main__':
    input_nums = [5, 7, 7, 8, 8, 10]
    input_target = 7
    solution = Solution()
    res = solution.searchRange(input_nums, input_target)
    print(res)
