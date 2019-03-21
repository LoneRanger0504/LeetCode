"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        """
        原理和path-sum i & ii类似
        只不过判断条件改成在到达叶子节点的时候，打印当前路径，再做一点小改动
        :param root:
        :return:
        """

        def search(root, path):
            if not root:
                return
            path.append(root.val)

            isLeaf = root.left == None and root.right == None
            if isLeaf:
                temp = ''
                for i in range(len(path)):
                    temp += str(path[i]) + '->'
                temp = temp[:-2]
                res.append(temp)

            if root.left != None:
                search(root.left, path)
            if root.right != None:
                search(root.right, path)
            path.pop()

        res = []
        path = []
        search(root, path)
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
    res = solution.binaryTreePaths(root)
    print(res)
