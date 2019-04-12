"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        双指针法，使用两个指针分别从首尾开始，如果两个指针对应的和等于target，直接返回[index1+1，index2+1]
        如果加起来大于target，则尾指针减1；如果小于target，则头指针加1
        因为数组已经是升序排列的了，每次的改动应该尽量按照变化小的方式改变指针位置
        """
        res = [-1, -1]
        if not numbers:
            return res
        start = 0
        end = len(numbers) - 1
        while start < end:
            num = numbers[start] + numbers[end]
            if num == target:
                res[0] = start + 1
                res[1] = end + 1
                return res
            elif num > target:
                end -= 1
            else:
                start += 1
        return res


if __name__ == '__main__':
    input_nums = [2, 7, 11, 15]
    input_target = 9
    solution = Solution()
    res = solution.twoSum(input_nums, input_target)
