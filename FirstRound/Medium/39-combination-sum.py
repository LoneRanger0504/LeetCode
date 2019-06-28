# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        回溯法写法思路：
        1. 定义全局结果数组
        2. 调用递归函数
        3. 返回全局结果数组
        4. 定义递归函数
            1) 参数，动态变化，一般为分支结果、限制条件等
            2) 终止条件，将分支结果添加到全局数组
            3) 剪枝条件
            4) 调用递归逐步产生结果，回溯搜索下一结果
        """

        def backtrack(temp, target):
            #  递归结束条件： target为0，temp未重复出现
            if target == 0 and sorted(temp) not in res:
                res.append(temp)
            #  因为每个元素可以重复使用，这里i每次都是从0到len(candidates)
            for i in range(len(candidates)):
                #  这里是回溯剪枝条件，当当前元素值大于当前target，表示下一次递归target会变成负数，
                #  而且由于数组已经是提前排序的，后面的值只会越来越大，因此则直接break
                if candidates[i] > target:
                    break
                backtrack(temp + [candidates[i]], target - candidates[i])

        res = []
        if not candidates or target <= 0:
            return res
        candidates.sort()
        backtrack([], target)
        return res


if __name__ == '__main__':
    input_candidates = [8, 7, 4, 3]
    input_target = 11
    solution = Solution()
    res = solution.combinationSum(input_candidates, input_target)
    print(res)
