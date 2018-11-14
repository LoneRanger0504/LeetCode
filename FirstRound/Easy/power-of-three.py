"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方
"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        首先判断是否为0，题目说的是整数，但没说是正整数，不能忘了0
        循环的方法和2的幂一样
        不用循环的解法：
        （1）找到int范围内最大的3的幂 3^19，只要n能够被其整除，则是3的幂
        （2）使用换底公式[log_a(b) = log_c(b) / log_c(a)]，
            所以log3(n) = lg(n) / lg(3) 这里好像只能用10为底，
            最后判断log3(n)是否为整数
        """
        # 循环做法：
        # if n == 0:
        #     return False
        # while n != 1:
        #     if n % 3 != 0:
        #         return False
        #     n = n / 3
        # return True

        # 换底公式做法：
        import math
        if n == 0:
            return False
        log_num = math.log10(n) / math.log10(3)
        if log_num - int(log_num) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    input_n = int(input())
    solution = Solution()
    result = solution.isPowerOfThree(input_n)
    print(result)
