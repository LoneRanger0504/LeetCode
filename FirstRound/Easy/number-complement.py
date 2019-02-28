"""
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

给定的整数保证在32位带符号整数的范围内。
你可以假定二进制数不包含前导零位。
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        (1)得到二进制表示，按位取反，再得到对应的值
        """
        temp = []
        binary = bin(num)
        val = binary[2:]
        res = 0
        for i in val:
            temp.append(int(i))
        for i in range(len(temp)):
            if temp[i] == 1:
                temp[i] = 0
            else:
                temp[i] = 1
        for i in range(len(temp)):
            res += 2 ** (len(temp) - i - 1) * temp[i]
        return res


if __name__ == '__main__':
    input_num = 3
    solution = Solution()
    res = solution.findComplement(input_num)
    print(res)
