"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        (1)循环做法：一直 mod 10取每一位的数字，加起来得到新的num，循环退出条件为 num < 10
        (2)非循环做法： return ((num-1) % 9 + 1) ???
        """
        while num >= 10:
            remainder = num % 10
            quotient = (num - remainder) / 10
            num = remainder + int(quotient)
        return num


if __name__ == '__main__':
    input_n = int(input())
    solution = Solution()
    result = solution.addDigits(input_n)
    print(result)
