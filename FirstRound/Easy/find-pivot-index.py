"""
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
"""
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        使用两个值来保存元素左边和右边的和，这里的左初始值为0
        从第一个元素开始，先更新右边和，再原有基础上减去当前元素即可
        与左边和比较，相等返回第一个。不相等更新左边和，加上当前元素
        """
        nums_len = len(nums)
        left = 0
        right = sum(nums[i] for i in range(nums_len))

        for i in range(nums_len):
            right = right - nums[i]
            if left != right:
                left = left + nums[i]
            else:
                return i
        return -1


if __name__ == '__main__':
    input_list = [-1, -1, 0, 1, 1, 0]
    solution = Solution()
    result = solution.pivotIndex(input_list)
    print(result)
