"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
给定N 求fib(N)
"""


class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        使用一个list来动态修改，根据前两个值更新对应的值
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        temp = [0] * (N + 1)
        temp[0] = 0
        temp[1] = 1
        for i in range(2, N + 1):
            temp[i] = temp[i - 2] + temp[i - 1]
        return temp[N]


if __name__ == '__main__':
    input_N = 4
    solution = Solution()
    res = solution.fib(input_N)
    print(res)
