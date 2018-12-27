"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
"""


class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        几种思路，最先想到的就是使用count(),按题意出现次数等于N即可，但是count函数需要遍历所有的元素，极端情况下，出现N次的数全在后一半，则速度受影响
        此题有一个关键点在于，数字总个数是N+1个，总次数是2N，但是有一个数出现了N次，其实剩下的N个数每个只出现了一次
        使用哈希表，简单的判断元素是否在keys中即可，出现次数大于1，则就是那个出现N次的数
        """
        for i in A:
            if A.count(i) == len(A) // 2:
                return i

        # dic = {}
        # for i in A:
        #     if i not in dic.keys():
        #         dic[i] = 1
        #     else:
        #         return i


if __name__ == '__main__':
    input_list = [1, 2, 3, 3]
    solution = Solution()
    res = solution.repeatedNTimes(input_list)
