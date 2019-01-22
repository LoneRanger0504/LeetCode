"""
给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。

在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
"""


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        判断下最大值减K与最小值加K之间的差值即可
        """
        min_value = min(A)
        max_value = max(A)
        res = (max_value - K) - (min_value + K)
        if res <= 0:
            return 0
        else:
            return res


if __name__ == '__main__':
    input_A = [1]
    input_K = 0
    solution = Solution()
    res = solution.smallestRangeI(input_A, input_K)
