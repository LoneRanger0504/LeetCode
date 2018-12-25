"""
给定两个表示复数的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。
"""


class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """
        对字符串进行分割，得到对应的实部和虚部，按照复数乘法规则相乘，最后按格式返回即可
        这里按照索引进行分割，还可以按 + 号进行split，对得到的list使用list的遍历取得实部和虚部
        """
        plus_index1 = a.index('+')
        i_index1 = a.index('i')
        plus_index2 = b.index('+')
        i_index2 = b.index('i')
        a1 = a[:plus_index1]
        b1 = a[plus_index1 + 1:i_index1]
        c1 = b[:plus_index2]
        d1 = b[plus_index2 + 1:i_index2]
        number_part = int(a1) * int(c1) - int(b1) * int(d1)
        complex_part = int(a1) * int(d1) + int(b1) * int(c1)
        return str(number_part) + '+' + str(complex_part) + 'i'


if __name__ == '__main__':
    input_a = '1+-1i'
    input_b = '1+-1i'
    solution = Solution()
    res = solution.complexNumberMultiply(input_a, input_b)
    print(res)
