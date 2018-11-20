"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        使用哈希表存储出现次数，再进行一个简单的筛选，时间复杂度为O(n)
        """
        dic = {}
        res = []
        nums_len = len(nums)
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        for i in dic.keys():
            if dic.get(i) > nums_len // 3:
                res.append(i)
        return res


if __name__ == '__main__':
    input_list = [1, 2, 3, 3]
    solution = Solution()
    result = solution.majorityElement(input_list)
    print(result)
