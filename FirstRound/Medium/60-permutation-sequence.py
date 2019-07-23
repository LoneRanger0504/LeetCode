# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
给定 n 和 k，返回第 k 个排列。
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        (1)全排列会超时
        (2)康拓展开
        """
        # import math
        # if n < 1 or n > 9 or k < 1 or k > math.factorial(n):
        #     return
        # _list = [i for i in range(1, n+1)]
        # res = []
        # visited = [0] * n
        # self.count = 0
        # def backtrack(temp, length):
        #     if length == n and self.count <= k:
        #         res.append(temp)
        #         self.count += 1
        #     for i in range(n):
        #         if visited[i] == 1:
        #             continue
        #         visited[i] = 1
        #         backtrack(temp + [_list[i]], length+1)
        #         visited[i] = 0
        # backtrack([], 0)
        # print(res)
        # result = res[k-1]
        # _str = ''
        # for i in result:
        #     _str += str(i)
        # return _str

        # (2)康拓展开
        import math
        nums = [i + 1 for i in range(n)]
        res = ''
        k = k - 1
        while n > 0:
            i = k // math.factorial(n - 1)
            k = k % math.factorial(n - 1)
            res += str(nums[i])
            nums.pop(i)
            n -= 1
        return res


if __name__ == '__main__':
    input_n = 9
    input_k = 24
    solution = Solution()
    res = solution.getPermutation(input_n, input_k)
    print(res)
