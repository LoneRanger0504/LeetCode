class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        栈的思想，先排除所有False 情况（长度为1或以右括号开头）
        对输入的字符串依次匹配，将所有的左括号压入栈中
        当栈不为空且当前的右括号与栈顶元素匹配，将栈顶元素出栈，否则返回False
        最后通过判断栈元素的个数是否为0来表示是否全部匹配
        """
        my_stack = []

        """
        这里最开始是用于判断左右括号，但是通过dic.values()或者dic.keys()可直接实现，不用重新定义list
        """
        # right_parenthenes = [')', '}', ']']
        # left_parentheses = ['(', '{', '[']

        parenthenes = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        """
        这里也不用多判断，在最后统一判断栈的长度是否为0即可
        """
        # if s == '':
        #     return True

        if len(s) == 1 or s[0] in parenthenes.keys():
            return False
        for i in s:
            if i in parenthenes.values():
                my_stack.append(i)
            elif my_stack != [] and parenthenes[i] == my_stack.pop():
                my_stack = my_stack[:len(my_stack)]
            else:
                return False
        return len(my_stack) == 0


if __name__ == '__main__':
    s = input()
    solution = Solution()
    flag = solution.isValid(s)
    print(flag)
