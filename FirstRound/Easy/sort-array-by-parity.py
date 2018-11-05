"""
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
"""


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        """
        使用双指针，交换奇数和偶数的位置，将所有的偶数交换到前面，while退出条件为start >= end
        """
        A_len = len(A)
        start = 0
        end = A_len - 1
        while start < end:
            if A[start] % 2 == 0:
                start += 1
            elif A[start] % 2 == 1 and A[end] % 2 == 1:
                end -= 1
            elif A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        return A


if __name__ == '__main__':
    input_list = [1, 3]
    solution = Solution()
    result = solution.sortArrayByParity(input_list)
    print(result)
