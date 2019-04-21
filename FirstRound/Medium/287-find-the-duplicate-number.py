"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        可以转为链表有环问题，需要判断两次，第一次两个指针相遇之后，快指针从0开始再走一遍，两个指针再次相遇的位置就重复数字对应的下标
        TODO：为什么就可以根据环来找到重复值呢？
        """
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                fast = 0
                while nums[slow] != nums[fast]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]


if __name__ == '__main__':
    input_nums = [1, 3, 4, 2, 2]
    solution = Solution()
    res = solution.findDuplicate(input_nums)
    print(res)
