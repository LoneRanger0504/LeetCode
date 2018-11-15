"""
给定一个Excel表格中的列名称，返回其相应的列序号
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        创建一个字典，对应字母与数字，但是其实可以用ASCII码来取，
        遍历字符串按照对应规则相加即可
        """
        dic = dict(A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8, I=9, J=10, K=11, L=12, M=13, N=14, O=15, P=16, Q=17, R=18,
                   S=19, T=20, U=21, V=22, W=23, X=24, Y=25, Z=26)
        s_len = len(s)
        num = 0
        for i in range(s_len):
            num += dic.get(s[i]) * 26 ** (s_len - i - 1)
        return num


if __name__ == '__main__':
    input_s = input()
    solution = Solution()
    result = solution.titleToNumber(input_s)
    print(result)
