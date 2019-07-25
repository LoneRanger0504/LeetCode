# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        def PowerWithUnsignedExponent(base, exponent):
            if exponent == 0:
                return 1
            if exponent == 1:
                return base
            result = PowerWithUnsignedExponent(base, exponent >> 1)
            result *= result
            if exponent & 1 == 1:
                result *= base
            return result

        #  注意在这里加上底数为0.0，指数小于0的情况，直接返回0.0
        #  浮点数比较等于不能直接用 == 或 ！=，需要借助一个很小的值epsinon，判断这个数在[-epsinon, epsinon]中间，表示等于0.0
        epsinon = 0.0000001
        if -epsinon <= base <= epsinon and exponent < 0:
            return 0.0
        flag = 1 if exponent > 0 else 0
        exponent = abs(exponent)
        res = PowerWithUnsignedExponent(base, exponent)
        if flag:
            return res
        else:
            return 1 / res


if __name__ == '__main__':
    input_base = 0.0
    input_exponent = -2
    solution = Solution()
    res = solution.Power(input_base, input_exponent)
    print(res)
