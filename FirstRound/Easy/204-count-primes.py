"""
统计所有小于非负整数 n 的质数的数量。
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        最常规的判断每个数是不是质数会超时，即使是只遍历到根号n加一
        厄拉多塞筛法：
        从2开始，把所有2的倍数位置置为0，接着下一个位置上不为0的数就是下一个质数，也就是3,
        再把3的所有倍数位置置为0，再重复，也就是5， 7， 11 。。。
        最后统计位置不为0的个数
        """
        if n < 3:
            return 0
        res = [1] * n
        res[0], res[1] = 0, 0
        import math
        for i in range(2, int(math.sqrt(n)) + 1):
            #  这一段就是将i的倍数位置置为0的操作，使用list的切片
            #  表示从i*i开始直到n,每隔i个位置上的数就置为0
            if res[i] == 1:
                res[i * i:n:i] = [0] * len(res[i * i:n:i])
        return res.count(1)


if __name__ == '__main__':
    input_n = 9999985
    solution = Solution()
    res = solution.countPrimes(input_n)
    print(res)
