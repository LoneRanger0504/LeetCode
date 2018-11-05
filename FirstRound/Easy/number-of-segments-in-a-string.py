class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        一开始想到的是正则表达式匹配，但其实用最基础的字符串的split()方法就可以
        split()以默认分隔符进行分割，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
        """
        import re
        re_pattern = '[a-z\\SA-Z]+'
        match = re.findall(re_pattern, s)
        if match:
            return len(match)
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    num = solution.countSegments(input())
    print(num)
