"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        统计1的个数
        """
        return bin(n)[2:].count('1')


if __name__ == '__main__':
    input_n = 5
    solution = Solution()
    res = solution.hammingWeight(input_n)
