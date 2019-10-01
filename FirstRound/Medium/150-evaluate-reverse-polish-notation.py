"""
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        """
        使用两个栈分别存放操作符和数字，根据不同情况入栈出栈，
        最后返回数字栈中的第一个值即可
        """
        if not tokens:
            return
        nums = []
        op = []
        for i in tokens:
            if i.isdigit():
                nums.append(int(i))
            elif i[0] == '-' and i[1:].isdigit():
                nums.append(-1 * int(i[1:]))
            else:
                a = nums.pop()
                b = nums.pop()
                if i == '+':
                    nums.append(a + b)
                elif i == '-':
                    nums.append((b - a))
                elif i == '*':
                    nums.append(a * b)
                else:
                    nums.append(int(b / a))
        return nums[0]


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    res = solution.evalRPN(tokens)
    print(res)
