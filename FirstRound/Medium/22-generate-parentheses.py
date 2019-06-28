# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        递归生成，需要判断何种情况是有效的括号(先添加左括号；保证左括号和右括号数量相等)
        括号数从多到少，每次递归先判断还能不能添加左括号，如果能，则继续添加
        如果不能添加了，再判断剩余右括号数是否大于剩余左括号数，大于，则添加右括号。
        """
        res = []

        def backtrack(left, right, temp):
            if left == 0 and right == 0:
                res.append(temp)
            if left > 0:
                backtrack(left - 1, right, temp + '(')
            if right > left:
                backtrack(left, right - 1, temp + ')')

        backtrack(n, n, '')
        return res


if __name__ == '__main__':
    input_n = 4
    solution = Solution()
    res = solution.generateParenthesis(input_n)
    print(res)
