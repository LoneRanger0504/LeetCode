"""
计算给定二叉树的所有左叶子之和。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        层次遍历，判断依据就是有左子节点，且左子节点是叶子节点
        也可以使用各种递归非递归的dfs，只需要注意判断是否是左叶子节点即可
        累加左叶子节点的值
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            size = len(queue)
            while size > 0:
                root = queue.pop(0)
                size -= 1
                if root.left:
                    queue.append(root.left)
                    if root.left.left is None and root.left.right is None:
                        res += root.left.val
                if root.right:
                    queue.append(root.right)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.sumOfLeftLeaves(root)
    print(res)
