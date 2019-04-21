"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        双指针，fast先往前走，如果两个位置的值不相等，更新slow=fast
        如果fast的值比slow大2，表示此时两个位置的值相等，但是重复数字超过两个，删除fast位置元素，将fast-1保持fast位于下一个元素
        """
        slow = fast = 0
        fast += 1
        while fast <= len(nums) - 1:
            if nums[slow] != nums[fast]:
                slow = fast
            else:
                if fast - slow == 2:
                    nums.remove(nums[fast])
                    fast -= 1
            fast += 1
        return len(nums)


if __name__ == '__main__':
    input_nums = [1, 1, 1]
    solution = Solution()
    res = solution.removeDuplicates(input_nums)
    print(res)
