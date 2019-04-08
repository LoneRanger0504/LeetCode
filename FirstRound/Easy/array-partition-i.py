"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
"""
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        将数组排序（注意python的数组排序方法.sort（）直接修改了原数组），每两个分为一组，每组的最小值相加就是最大子序和，即下标从0开始的偶数位数相加
        为什么这里最大子序和就是偶数位数字呢？？？
        """
        nums.sort()
        res = 0
        for num in nums[::2]:
            res += num
        return res


if __name__ == '__main__':
    input_arr = [1, 2, 4, 3]
    solution = Solution()
    result = solution.arrayPairSum(input_arr)
    print(result)
