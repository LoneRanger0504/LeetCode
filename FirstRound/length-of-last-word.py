class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        使用了正则表达式中的findall(),找到字符串中的所有非空格字符，即大小写单词，返回到match列表中
        则返回match列表中的最后一个字符串的长度即可
        """
        import re
        re_pattern = '[a-zA-Z]+'
        match = re.findall(re_pattern, s)
        if match:
            return len(match[-1])
        else:
            return 0


if __name__ == '__main__':
    input_str = input()
    solution = Solution()
    last_word_length = solution.lengthOfLastWord(input_str)
    print(last_word_length)
