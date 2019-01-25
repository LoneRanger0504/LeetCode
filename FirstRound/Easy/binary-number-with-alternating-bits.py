"""
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        (1)低效方法：得到二进制表示遍历判断相邻位是否相等
        (2)temp = n^(n>>1) 
            return(temp&(temp+1)) == 0 
        """
        # binary = bin(n)[2:]
        # for i in range(len(binary) - 1):
        #     if binary[i] == binary[i + 1]:
        #         return False
        # return True
        temp = n ^ (n >> 1)
        a = n >> 1
        return temp & (temp + 1) == 0


if __name__ == '__main__':
    input_n = 5
    solution = Solution()
    res = solution.hasAlternatingBits(input_n)
    print(res)
