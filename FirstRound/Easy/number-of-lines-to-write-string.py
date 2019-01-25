"""
我们要把给定的字符串 S 从左到右写到每一行上，每一行的最大宽度为100个单位，如果我们在写某个字母的时候会使这行超过了100 个单位，那么我们应该把这个字母写到下一行。我们给定了一个数组 widths ，这个数组 widths[0] 代表 'a' 需要的单位， widths[1] 代表 'b' 需要的单位，...， widths[25] 代表 'z' 需要的单位。

现在回答两个问题：至少多少行能放下S，以及最后一行使用的宽度是多少个单位？将你的答案作为长度为2的整数列表返回。
"""


class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        """
        遍历S将对应的单位累加，超过100，行数加1，将加起来超过100的那个值作为新的开始，即从下一行开始继续加
        """
        res = [0] * 2
        start = ord('a')
        count = 0
        line = 1
        for i in S:
            count += widths[ord(i) - start]
            if count > 100:
                line += 1
                count = 0
                count += widths[ord(i) - start]

        res[0] = line
        res[1] = count
        return res


if __name__ == '__main__':
    input_widths = [7, 5, 4, 7, 10, 7, 9, 4, 8, 9, 6, 5, 4, 2, 3, 10, 9, 9, 3, 7, 5, 2, 9, 4, 8, 9]
    input_S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
    solution = Solution()
    res = solution.numberOfLines(input_widths, input_S)
    print(res)
