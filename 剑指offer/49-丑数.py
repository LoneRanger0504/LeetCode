"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        res = [1] * index
        next_index = 1
        M2 = 0
        M3 = 0
        M5 = 0
        while next_index < index:
            res[next_index] = min(res[M2] * 2, res[M3] * 3, res[M5] * 5)
            while res[M2] * 2 <= res[next_index]:
                M2 += 1
            while res[M3] * 3 <= res[next_index]:
                M3 += 1
            while res[M5] * 5 <= res[next_index]:
                M5 += 1
            next_index += 1
        return res[-1]


if __name__ == '__main__':
    input_index = 10
    solution = Solution()
    res = solution.GetUglyNumber_Solution(input_index)
    print(res)