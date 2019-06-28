# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
所有数字都是正整数。
解集不能包含重复的组合。 
输入: k = 3, n = 7
输出: [[1,2,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        """
        回溯法+剪枝
        递归结束条件： k, n都为0，且temp排序列表未重复出现
        递归过程中为了保证下标不重复，每次从当前下标加1开始，同时这题还限制了只能用1-9，因此range的范围就是(index+1, 10)
        """

        def backtrack(index, temp, num, target):
            if target == 0 and num == 0 and sorted(temp) not in res:
                res.append(temp)
            if target < 0:
                return

            for i in range(index + 1, 10):
                backtrack(i, temp + [i], num - 1, target - i)

        if k < 0 or n < 0:
            return []
        res = []
        backtrack(0, [], k, n)
        return res


if __name__ == '__main__':
    input_k = 3
    input_n = 19
    solution = Solution()
    res = solution.combinationSum3(input_k, input_n)
    print(res)
