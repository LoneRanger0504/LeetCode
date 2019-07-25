# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here

        def isSubTree(root1, root2):
            if not root2:
                return True
            if not root1:
                return False
            if root1.val != root2.val:
                return False
            return isSubTree(root1.left, root2.left) and isSubTree(root1.right, root2.right)

        has_subtree = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                has_subtree = isSubTree(pRoot1, pRoot2)
            if not has_subtree:
                has_subtree = self.HasSubtree(pRoot1.left, pRoot2)
            if not has_subtree:
                has_subtree = self.HasSubtree(pRoot1.right, pRoot2)
        return has_subtree


if __name__ == '__main__':
    root1 = TreeNode(8)
    root1.left = TreeNode(8)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(9)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(4)
    root1.left.right.right = TreeNode(7)
    root2 = TreeNode(8)
    root2.left = TreeNode(9)
    root2.right = TreeNode(2)
    solution = Solution()
    res = solution.HasSubtree(root1, root2)
    print(res)
