# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
在一个长度为n+1的数组里所有的数字都在1~n范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组
输入示例： [2， 3， 5， 4， 3， 2， 6， 7]
"""


class Solution:
    def findDuplicate(self, nums):
        """
        :param nums:
        :return:
        """
        """
        (1)可以转为链表有环问题，需要判断两次，第一次两个指针相遇之后，快指针从0开始再走一遍，两个指针再次相遇的位置就重复数字对应的下标
        (2)剑指offer解法(目前存在问题)
        """
        # if not nums:
        #     return
        # fast, slow = 0, 0
        # while True:
        #     fast = nums[nums[fast]]
        #     slow = nums[slow]
        #     if fast == slow:
        #         fast = 0
        #         while nums[fast] != nums[slow]:
        #             fast = nums[fast]
        #             slow = nums[slow]
        #         return nums[slow]
        if not nums:
            return

        def countRange(start, end):
            if not nums:
                return
            count = 0
            for i in range(len(nums)):
                if start <= nums[i] <= end:
                    count += 1
            return count

        start = 0
        end = len(nums)
        while end >= start:
            mid = (end - start) >> 1 + start
            count = countRange(start, mid)
            if end == start:
                if count > 1:
                    return start
                else:
                    break
            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1
        return -1


if __name__ == '__main__':
    input_nums = [2, 3, 5, 4, 3, 2, 6, 7]
    solution = Solution()
    res = solution.findDuplicate(input_nums)
    print(res)
