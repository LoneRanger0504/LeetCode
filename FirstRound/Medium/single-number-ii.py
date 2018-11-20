"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
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
        （1）类比之前的只出现一次的数字1中，使用set去重之后，对数组的和做差，总是有规律可循，这里就是乘以3减去原数组和，再除2就得到只出现一次的数字
        （2）使用哈希表，但是占用额外存储空间
        """
        return int((sum(set(nums)) * 3 - sum(nums)) / 2)
        # 哈希表：
        # dic = {}
        # for i in nums:
        #     if i in dic.keys():
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # for j in dic.keys():
        #     if dic.get(j) == 1:
        #         return j


if __name__ == '__main__':
    input_list = [2, 2, 3, 2]
    solution = Solution()
    result = solution.singleNumber(input_list)
    print(result)
