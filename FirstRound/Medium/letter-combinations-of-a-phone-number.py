"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        """
        构建字典，对输入的字符串遍历，得到n个list，使用python自带的笛卡尔积实现方法。
        如果不使用自带的笛卡尔积，待补充递归解法
        """
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        import itertools
        res = []
        input_list = []
        if digits == '':
            return res
        for i in digits:
            input_list.append(dic.get(i))
        for i in itertools.product(*input_list):
            temp = ''.join(i)
            res.append(temp)
        return res


if __name__ == '__main__':
    input_digits = '234'
    solution = Solution()
    res = solution.letterCombinations(input_digits)
    print(res)
