"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        根据空格进行分隔，再对每个字符串倒序输出
        但是并没有达到最优解，因为新建了一个列表
        """
        new_list = [i[::-1] for i in s.split(' ')]
        return ' '.join(new_list)


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseWords(input())
    print(result)
