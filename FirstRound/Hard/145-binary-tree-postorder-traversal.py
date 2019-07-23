# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉树，返回它的 后序 遍历。使用递归和非递归
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # (1)递归实现后序遍历
        # def postorder(root):
        #     if not root:
        #         return
        #     if root.left != None:
        #         postorder(root.left)
        #     if root.right != None:
        #         postorder(root.right)
        #     res.append(root.val)
        #
        # res = []
        # if not root:
        #     return res
        # postorder(root)
        # return res
        # (2)非递归实现后序遍历
        #  使用一个栈，实现后进先出
        #  添加的时候按照根节点，左子树，右子树添加，取出的时候弹出栈顶元素
        #  最后再把res逆序输出
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            root = queue.pop(-1)
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return res[::-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    res = solution.postorderTraversal(root)
    print(res)
