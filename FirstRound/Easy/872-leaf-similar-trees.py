"""
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        """
        dfs遍历分别得到两棵树的叶子节点的list,判断是否相等即可
        """

        def dfs(root, leaves):
            if not root:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return root

        if not root1 or not root2:
            return False
        leaves1 = []
        leaves2 = []
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2


if __name__ == '__main__':
    root1 = TreeNode(3)
    root2 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)
    solution = Solution()
    res = solution.leafSimilar(root1, root2)
    print(res)
