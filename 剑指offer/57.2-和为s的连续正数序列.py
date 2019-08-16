"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        res = []
        small = 1
        big = 2
        mid = (tsum + 1) / 2
        cur_sum = small + big
        while small < mid:
            if cur_sum == tsum:
                res.append([i for i in range(small, big+1)])
            while cur_sum > tsum and small < mid:
                cur_sum -= small
                small += 1
                if cur_sum == tsum:
                    res.append([i for i in range(small, big+1)])
            big += 1
            cur_sum += big
        return res


if __name__ == '__main__':
    input_tsum = 5
    solution = Solution()
    res = solution.FindContinuousSequence(input_tsum)
    print(res)