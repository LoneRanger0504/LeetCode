"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 2^31.
"""


def num2bin(num):
    count = 0
    binary_list = []
    while num != 0:
        quotient = num % 2
        num = (num - quotient) // 2
        binary_list.append(str(quotient))
        if quotient == 1:
            count += 1
    binary_list.reverse()
    list_len = len(binary_list)
    padding_num = 32 - list_len
    binary = '0' * padding_num + ''.join(binary_list)
    return binary


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        """
        (1)低效方法：得到每个输入的二进制表达，按位对比，这里x y小于2^31，使用32位表示二进制
        (2)得到x y的二进制，直接使用x异或y，统计1的次数，bin(x^y).count('1')
        """
        x_binary = num2bin(x)
        y_binary = num2bin(y)
        count = 0
        for i in range(len(x_binary)):
            if x_binary[i] != y_binary[i]:
                count += 1
        return count
