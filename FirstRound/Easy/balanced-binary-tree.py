"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        递归获取树的高度，每次判断是否平衡，但是会存在重复计算，时间效率低
        另一种在计算高度的时候时刻判断是否平衡
        """

        #  递归计算左右子树高度再判断
        # def treeDepth(root):
        #     if not root:
        #         return 0
        #     left = treeDepth(root.left)
        #     right = treeDepth(root.right)
        #     depth = max(left, right)
        #     return depth + 1
        # if not root:
        #     return True
        # left_height = treeDepth(root.left)
        # right_height = treeDepth(root.right)
        # difference = abs(left_height - right_height)
        # if difference > 1:
        #     return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        def validate(root):
            if root is None:
                return True, 0

            balanced, leftHeight = validate(root.left)
            if not balanced:
                return False, 0
            balanced, rightHeight = validate(root.right)
            if not balanced:
                return False, 0

            return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1

        balanced, _ = validate(root)
        return balanced


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = root.left.right = TreeNode(3)
    root.left.left.left = root.left.left.right = TreeNode(4)
    solution = Solution()
    res = solution.isBalanced(root)
    print(res)
