"""
给定一个二叉树，在树的最后一行找到最左边的值。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        还是层次遍历，只不过这里做了一点小变动，遍历每一行的时候，先添加右节点，再添加左节点
        这样遍历完整个list的最后一个值就是最后一行的最左边的子节点也就是树最左下角的值
        """
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            while size > 0:
                root = queue.pop(0)
                res.append(root.val)
                size -= 1
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
        return res[-1]


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    input_val = 5
    solution = Solution()
    res = solution.findBottomLeftValue(root)
    print(res)
