"""
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        用set找到缺失的数字，对原本的等差数组求和，减去nums的和，就是缺失的数字和重复数字的差
        用缺失数字减去差值即可
        """
        nums_len = len(nums)
        res = [0] * 2
        num_list = [i for i in range(1, nums_len + 1)]
        for i in set(num_list) - set(nums):
            res[1] = i
        difference = (nums_len * (nums_len + 1) / 2) - sum(nums)
        res[0] = res[1] - difference
        return res


if __name__ == '__main__':
    input_list = [1, 1]
    solution = Solution()
    res = solution.findErrorNums(input_list)
    print(res)
