"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            if i == popV[0]:
                stack.pop()
                popV.pop(0)
        for j in popV:
            if j == stack[-1]:
                stack.pop()
        return stack == []


if __name__ == '__main__':
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    solution = Solution()
    res = solution.IsPopOrder(pushV, popV)
    print(res)