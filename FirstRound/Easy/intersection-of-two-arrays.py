"""
给定两个数组，编写一个函数来计算它们的交集。
"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        使用set去余，为了减少时间复杂度，判断两个list的长度，遍历短的list判断元素是否也在另一个list中
        但是set()实现了取交集，直接set1 & set2即可，无需再转为list
        """
        set_1 = list(set(nums1))
        set_2 = list(set(nums2))
        set1_len = len(set_1)
        set2_len = len(set_2)
        res = []
        if set1_len <= set2_len:
            for i in range(set1_len):
                if set_1[i] in set_2:
                    res.append(set_1[i])
        else:
            for i in range(set2_len):
                if set_2[i] in set_1:
                    res.append(set_2[i])
        return res


if __name__ == '__main__':
    input_list1 = [1, 2, 2, 1]
    input_list2 = [2, 2]
    solution = Solution()
    result = solution.intersection(input_list1, input_list2)
    print(result)
