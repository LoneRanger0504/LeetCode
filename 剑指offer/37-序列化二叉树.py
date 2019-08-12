# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
请实现两个函数，分别用来序列化和反序列化二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        # write code here
        def dfs(root):
            if not root:
                self.res += '$,'
                return
            self.res += str(root.val) + ','
            dfs(root.left)
            dfs(root.right)

        self.res = ''
        if not root:
            self.res += '$,'
            return self.res
        dfs(root)
        return self.res

    def Deserialize(self, s):
        # write code here
        def helper(node_list):
            if not node_list:
                return
            val = node_list.pop(0)
            if val == '$':
                return
            root = TreeNode(int(val))
            root.left = helper(node_list)
            root.right = helper(node_list)
            return root

        node_list = s.split(',')
        return helper(node_list)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    solution = Solution()
    s = solution.Serialize(root)
    res = solution.Deserialize(s)
    print(s)
    print(res)
