"""
给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。
"""


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        """
        比较直接的方法，依据题目条件，只有一个字母，返回TRUE
        如果第一个字母是大写，第二个也为大写，则后面不应该出现小写，出现返回FALSE
        如果第一个为大写，第二个为小写，从第二个开始遍历，如果出现大写则返回FALSE
        但是其实Python的字符串方法中.isupper()和.islower()可以直接对整个字符串作用
        还有一个.istitle()表示首字母大写，可以直接写成如下代码：
        return word.isupper() or word.islower() or word.istitle()
        """

        if len(word) == 1:
            return True
        if word[0].isupper() and word[1].isupper():
            for i in word[2::]:
                if i.islower():
                    return False
        else:
            for i in word[1::]:
                if i.isupper():
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.detectCapitalUse(input())
    print(result)
