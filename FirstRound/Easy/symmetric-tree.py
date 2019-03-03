"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        (1)递归解法：
        定义一个isMirror函数，递归判断前序遍历和对称前序遍历每一步的val是否相等
        这里的对称前序遍历表示每次先遍历根节点再遍历右子节点最后遍历左子节点
        最开始的输入参数是两个root
        (2)循环解法：
        使用栈来辅助实现层次遍历，同样使用两个root分别模拟前序遍历和对称前序遍历
        """

        def ismirror(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return ismirror(root1.left, root2.right) and ismirror(root1.right, root2.left)

        return ismirror(root, root)
