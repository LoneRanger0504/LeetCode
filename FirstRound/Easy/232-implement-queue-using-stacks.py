# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        """
        初始化两个栈分别作为入栈和出栈
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        """
        插入只需要将元素插入入栈即可
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        """
        出栈时，则需要考虑出栈是否为空。
        当出栈为空，将入栈中的所有元素添加到出栈中，再弹出栈顶元素
        """
        if len(self.stack2) <= 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
        return self.stack2.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        """
        与pop操作相同，需要先判断出栈是否为空再返回栈顶元素
        """
        if not self.stack2:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop(-1))
        element = self.stack2[-1]
        return element

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        """
        需要确保出栈和入栈都不为空
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    x_1 = 3
    x_2 = 4
    obj = MyQueue()
    obj.push(x_1)
    obj.push(x_2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)
