"""
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        后续遍历，先左再右再根，这样就能得到一个根节点的左右子树的和
        根据题意，坡度就是左右子树和的差的绝对值，使用一个list保存最后累加即可
        这里递归返回的是左右子树的和与当前节点的和，也就是以当前节点为根节点的子树的和
        """

        def dfs(root, tilt):
            if not root:
                return 0
            left = dfs(root.left, tilt)
            right = dfs(root.right, tilt)
            res.append(abs(left - right))
            return root.val + left + right

        if not root:
            return 0
        tilt = 0
        res = []
        dfs(root, tilt)
        return sum(res)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    solution = Solution()
    res = solution.findTilt(root)
    print(res)
