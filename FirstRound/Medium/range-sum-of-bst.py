"""
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。
输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        """
        (1)直接但效率稍低的解法：递归遍历二叉搜索树，当L <= root.val <= R，加到辅助list中，最后返回sum(list)
        (2)利用二叉搜索树的性质，根节点大于左子树的最大值，小于右子树中的最小值，因此，当root.val 
        """
        #  (1)直接递归遍历
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     if L <= root.val <= R:
        #         res.append(root.val)
        #     dfs(root.right)
        # res = []
        # if not root:
        #     return
        # dfs(root)
        # return sum(res)
        #  (2)利用性质剪枝
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    solution = Solution()
    res = solution.rangeSumBST(root, 7, 15)
    print(res)
