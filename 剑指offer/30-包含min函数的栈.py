# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.val_stack = []
        self.helper_stack = []

    def push(self, node):
        # write code here
        self.val_stack.append(node)
        if len(self.helper_stack) == 0:
            self.helper_stack.append(node)
        elif node < self.helper_stack[-1]:
            self.helper_stack.append(node)
        else:
            self.helper_stack.append(self.helper_stack[-1])

    def pop(self):
        # write code here
        if len(self.helper_stack) <= 0:
            return
        else:
            self.val_stack.pop()
            self.helper_stack.pop()

    def top(self):
        # write code here
        if len(self.helper_stack) <= 0:
            return
        return self.helper_stack[-1]

    def min(self):
        # write code here
        return self.top()


if __name__ == '__main__':
    solution = Solution()
    solution.push(3)
    num1 = solution.min()
    solution.push(2)
    num2 = solution.min()
    solution.pop()
    num3 = solution.min()
    print(num1, num2, num3)
