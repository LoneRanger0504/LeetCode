"""
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。
"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        找到最大值，再将数组排序得到第二大值，根据条件比较
        """
        nums_len = len(nums)
        if nums_len < 2:
            return 0
        else:
            max = 0
            max_index = 0
            for i in range(nums_len):
                if nums[i] > max:
                    max = nums[i]
                    max_index = i
            nums.sort()
            if max >= nums[-2] * 2:
                return max_index
            else:
                return -1

            # max_value = max(nums)
            # max_index = nums.index(max_value)
            # nums.sort()
            # if max_value >= nums[-2] * 2:
            #     return max_index
            # else:
            #     return -1


if __name__ == '__main__':
    input_list = [3, 6, 1, 0]
    solution = Solution()
    result = solution.dominantIndex(input_list)
    print(result)
