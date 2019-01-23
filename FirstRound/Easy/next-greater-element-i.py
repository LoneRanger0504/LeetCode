"""
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        (1)用一个字典保存nums1中的元素大小和在nums2中的位置
        再遍历判断是否满足题意
        (2)使用栈的特性，直到找到大于该值的值，放到字典中，
        返回的时候遍历nums1的值，使用dic.get(key, default=None)可以设置不在字典中的键的值为-1，表示在nums2中没有在他之后比他大的值
        """
        res = []
        dic = {}
        for i in nums1:
            dic[i] = nums2.index(i)
        for key in dic.keys():
            index = dic.get(key)
            count = 0
            for j in range(index, len(nums2)):
                if nums2[j] > key:
                    count += 1
                    res.append(nums2[j])
                    break
                else:
                    continue
            if count == 0:
                res.append(-1)
        return res

    # stack = []
    # dic = {}
    # for num in nums2:
    #     while stack and num > stack[-1]:
    #         dic[stack.pop()] = num
    #     stack.append(num)
    # return [dic.get(num, -1) for num in nums1]


if __name__ == '__main__':
    input_nums1 = [4, 2, 1, 3]
    input_nums2 = [1, 2, 3, 4, 5]
    solution = Solution()
    res = solution.nextGreaterElement(input_nums1, input_nums2)
    print(res)
