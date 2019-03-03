"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 使用list模拟栈，创建一个数据栈一个辅助栈
        # 数据栈用于压栈保存数据，辅助栈用于保存最小值和次小值
        self.val_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        # 数据栈进行常规的入栈操作，使用append()模拟
        self.val_stack.append(x)
        # 辅助栈需要判断，只有当辅助栈为空或者待压入的值小于辅助栈的栈顶，才将value压入辅助栈
        # 否则将当前栈顶元素压栈
        if len(self.temp_stack) == 0 or x < self.temp_stack[-1]:
            self.temp_stack.append(x)
        else:
            self.temp_stack.append(self.temp_stack[-1])

    def pop(self) -> None:
        # 出栈操作就使用pop()
        self.val_stack.pop()
        self.temp_stack.pop()

    def top(self) -> int:
        # 返回数据栈的栈顶元素，注意这里使用-1来防止越界
        return self.val_stack[-1]

    def getMin(self) -> int:
        # 辅助栈的栈顶元素即为当前数据栈中的最小元素
        return self.temp_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
