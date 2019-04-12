"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        整体思路：利用异或原理，将数组分为两个子数组，每个子数组各包含一个只出现一次的数字
        划分依据为：某一位是否为1，这个位数由整个nums第一遍异或得到的值确定
        findFirst1()作用为找到入参num的第一个为1的位数
        isBit1()作用为按照findFirst1()找到的index进行子数组划分
        分成两个子数组后，则再次分别异或，即可得到对应的只出现一次的数字
        """

        def findFirst1(num):
            indexBit = 0
            while num & 1 == 0 and indexBit < 32:
                num = num >> 1
                indexBit += 1
            return indexBit

        def isBit1(num, indexBit):
            num = num >> indexBit
            return num & 1

        res = []
        if not nums:
            return res
        # 得到异或的最后的值
        or_num = 0
        for i in nums:
            or_num ^= i
        # 找到异或值中第一个1对应的位
        index_of_1 = findFirst1(or_num)
        # 按照对应位上是否为1分为两个子数组，分别进行异或操作，即可得到出现一次的两个数
        num1 = num2 = 0
        for i in nums:
            if isBit1(i, index_of_1):
                num1 = num1 ^ i
            else:
                num2 = num2 ^ i
        res.append(num1)
        res.append(num2)
        return res


if __name__ == '__main__':
    input_nums = [1, 2, 1, 3, 2, 5]
    solution = Solution()
    res = solution.singleNumber(input_nums)
    print(res)
