"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方
"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        首先判断是否为0，题目说的是整数，但没说是正整数，不能忘了0
        然后对n有：如果n是奇数，则肯定不是2的幂，n是偶数，n = n / 2，一直判断到 n = 1，如果最后n=1,则就是2的幂
        但是有一种最快解法： return n & (n-1) == 0 
        因为2的幂的二进制表示最高位是1，其余全是0， n-1则是最高位是0，其余位是1
        两者相与
        """
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = int(n / 2)
        return True


if __name__ == '__main__':
    input_n = int(input())
    solution = Solution()
    result = solution.isPowerOfTwo(input_n)
    print(result)
