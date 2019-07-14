# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)


if __name__ == '__main__':
    input_node = [1, 2, 3]
    solution = Solution()
    for node in input_node:
        solution.push(input_node)
        res = solution.pop()
        print(res)
