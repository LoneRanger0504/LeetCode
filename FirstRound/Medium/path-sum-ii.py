"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        """
        打印所有满足题意的路径，原理同path-sum
        只需要再到达每个节点的时候，判断一下当前节点的值是否等于传入的sum,等于就复制一个path添加到res
        不等于就依次遍历左右子树，每次更新sum = sum - root.val
        最后pop()一下
        """

        def findPath(root, path, sum):
            if not root:
                return
            path.append(root.val)

            isLeaf = root.left == None and root.right == None
            if root.val == sum and isLeaf:
                temp = [i for i in path]
                res.append(temp)

            if root.left != None:
                findPath(root.left, path, sum - root.val)
            if root.right != None:
                findPath(root.right, path, sum - root.val)
            path.pop()

        res = []
        path = []
        findPath(root, path, sum)
        return res


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    solution = Solution()
    res = solution.pathSum(root, 22)
    print(res)
