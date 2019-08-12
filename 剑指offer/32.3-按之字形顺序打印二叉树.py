# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        res = []
        if not pRoot:
            return res
        queue1 = [pRoot]
        queue2 = []
        while queue1 or queue2:
            temp1 = []
            temp2 = []
            size1 = len(queue1)
            while size1 > 0:
                root = queue1.pop()
                temp1.append(root.val)
                size1 -= 1
                if root.left:
                    queue2.append(root.left)
                if root.right:
                    queue2.append(root.right)
            if temp1:
                res.append(temp1)
            size2 = len(queue2)
            while size2:
                root = queue2.pop()
                temp2.append(root.val)
                size2 -= 1
                if root.right:
                    queue1.append(root.right)
                if root.left:
                    queue1.append(root.left)
            if temp2:
                res.append(temp2)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(5)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.Print(root)
    print(res)
