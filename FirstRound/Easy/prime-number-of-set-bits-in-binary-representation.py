"""
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）
"""


def isPrime(num):
    import math
    for j in range(2, int(math.sqrt(num) + 1)):
        if num % j == 0:
            return False
    return True


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        """
        生成list保存L到R+1的值，转换成二进制，再统计1的个数
        根据1的个数判断是不是质数，质数判断法：从2到(n^0.5)+1遍历,存在能够被n整除的数就不是质数。
        使用一个辅助列表减少质数判断次数
        """
        nums = [i for i in range(L, R + 1)]
        res = 0
        prime_num = []
        for i in nums:
            count = bin(i)[2:].count('1')
            if count < 2:
                continue
            elif count not in prime_num:
                flag = isPrime(count)
                if flag:
                    prime_num.append(count)
                    res += 1
            else:
                res += 1
        return res


if __name__ == '__main__':
    input_L = 842
    input_R = 888
    solution = Solution()
    res = solution.countPrimeSetBits(input_L, input_R)
    print(res)
