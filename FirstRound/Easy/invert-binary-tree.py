"""
翻转一棵二叉树。(求一棵树的镜像)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        先判空，再交换左右子树，深度优先遍历，递归地交换左右子树
        从而实现反转一棵树
        """
        if root == None:
            return
        # 交换左右子树
        temp = root.left
        root.left = root.right
        root.right = temp
        # 递归
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
