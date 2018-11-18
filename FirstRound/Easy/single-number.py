"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        最蠢的遍历在极端情况下会超时
        解决办法：
        （1）使用哈希表，这题分类也是哈希表，遍历数组，统计每个元素出现的次数，按照<元素，出现次数>构建哈希表
        最后再找到那个value为1的值，但是使用了额外的存储空间
        （2）异或  相同的值异或为0，0异或任何值为任何值，异或具有交换性
        因此我们只需要对数组的每个元素进行遍历，进行异或，相同的两个值会异或变成0，最后只剩下只出现一次的数字
        (3)因为这题只有一个单独元素，使用set()去重之后将和乘以2再减去原数组的和，就是单独的那个数字
        """
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    input_list = [2, 2, 1]
    solution = Solution()
    result = solution.singleNumber(input_list)
