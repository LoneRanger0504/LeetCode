"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        （1）直观的思路：使用一个哈希表，遍历元素，出现重复的键值返回ture，否则返回false
        （2）使用set()去重，判断去重后的新数组与原数组的长度是否相等，相等返回false，不相等即存在重复元素，返回true。
        """
        dic = {}
        for i in nums:
            if i in dic.keys():
                return True
            else:
                dic[i] = 1
        return False


if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 1]
    solution = Solution()
    result = solution.containsDuplicate(input_list)
    print(result)
