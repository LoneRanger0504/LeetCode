"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        """
        把A和B拼接起来得到一个新的字符串，为了按照空格分割，加上空格连接
        按照空格分割，返回只出现一次的字符串即可
        """
        C = A + ' ' + B
        C_list = C.split(' ')
        res = []
        for i in C_list:
            if C_list.count(i) == 1:
                res.append(i)
        return res


if __name__ == '__main__':
    input_A = "the apple is sweet"
    input_B = "the apple is sour"
    solution = Solution()
    res = solution.uncommonFromSentences(input_A, input_B)
