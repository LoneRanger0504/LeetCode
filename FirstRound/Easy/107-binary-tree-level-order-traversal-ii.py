"""
给定一个二叉树，返回其节点值自底向上的层次遍历。
（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        还是借助队列实现层次遍历，把最后的list反转一下即可得到自底向上的遍历结果
        """
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                root = queue.pop(0)
                temp.append(root.val)
                size -= 1
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(temp)
        return res[::-1]


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    input_val = 5
    solution = Solution()
    res = solution.levelOrderBottom(root)
    print(res)
