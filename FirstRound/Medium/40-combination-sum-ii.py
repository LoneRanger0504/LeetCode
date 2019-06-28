# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。
说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        由于每个元素只能使用一次，需要使用visited数组辅助标识，
        在递归过程中判断，如果当前位置已经被访问过或者当前位置的值与前一个位置的值相同，且前一个位置未被访问过，
        则应该跳过当前位置，确保不会重复使用有重复的元素
        """

        def backtrack(temp, target):
            if target == 0 and sorted(temp) not in res:
                res.append(temp)
            for i in range(len(candidates)):
                if visited[i] == 1 or (i > 0 and candidates[i] == candidates[i - 1] and visited[i - 1] == 0):
                    continue
                if candidates[i] > target:
                    break
                visited[i] = 1
                backtrack(temp + [candidates[i]], target - candidates[i])
                visited[i] = 0

        res = []
        if not candidates or target <= 0:
            return res
        visited = [0] * len(candidates)
        candidates.sort()
        backtrack([], target)
        return res


if __name__ == '__main__':
    input_candidates = [2, 5, 2, 1, 2]
    input_target = 8
    solution = Solution()
    res = solution.combinationSum2(input_candidates, input_target)
    print(res)
