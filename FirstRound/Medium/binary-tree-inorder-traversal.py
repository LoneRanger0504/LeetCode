# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉树，返回它的中序 遍历。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # （1）递归实现中序遍历
        def inorder(root):
            if not root:
                return
            if root.left != None:
                inorder(root.left)
            res.append(root.val)
            if root.right != None:
                inorder(root.right)

        res = []
        if not root:
            return res
        inorder(root)
        return res
        # (2)TODO:中序非递归


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    res = solution.inorderTraversal(root)
    print(res)
