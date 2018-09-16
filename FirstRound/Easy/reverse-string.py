"""
编写一个函数，其作用是将输入的字符串反转过来。
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        直接逆序输出
        """
        return s[::-1]


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseString(input())
    print(result)
