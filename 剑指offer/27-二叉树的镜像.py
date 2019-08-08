"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and  not root.right:
            return
        res = root.left
        root.left = root.right
        root.right = res
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    solution = Solution()
    solution.Mirror(root)
