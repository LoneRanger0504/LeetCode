"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        按题意判断即可，先判断能否整除15再依次判断
        """
        temp = [i for i in range(1, n + 1)]
        for i in range(len(temp)):
            if temp[i] % 15 == 0:
                temp[i] = 'FizzBuzz'
            elif temp[i] % 3 == 0:
                temp[i] = 'Fizz'
            elif temp[i] % 5 == 0:
                temp[i] = 'Buzz'
            else:
                temp[i] = str(temp[i])
        return temp
