"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
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
    print(binary)
    return count


class Solution:

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        """
        (1)自定义一个计数二进制中1的个数的函数
        (2)res[i] += res[i&(i-1)] + 1
        """
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = num2bin(i)
        return res


if __name__ == '__main__':
    input_num = 10
    solution = Solution()
    res = solution.countBits(input_num)
    print(res)
