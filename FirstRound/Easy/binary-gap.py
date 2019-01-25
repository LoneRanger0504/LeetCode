"""
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。

如果没有两个连续的 1，返回 0 。

"""


class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        先将二进制表示中1的下标保存到辅助list，遍历辅助list维护一个最大差值difference即可
        """
        binary = bin(N)[2:]
        index = []
        for i in range(len(binary)):
            if binary[i] == '1':
                index.append(i)
        max_val = 0
        for i in range(len(index) - 1):
            difference = index[i + 1] - index[i]
            if difference > max_val:
                max_val = index[i + 1] - index[i]
        return max_val


if __name__ == '__main__':
    input_N = 18
    solution = Solution()
    res = solution.binaryGap(input_N)
    print(res)
