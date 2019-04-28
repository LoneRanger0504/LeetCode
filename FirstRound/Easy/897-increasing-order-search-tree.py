"""
给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，
并且每个结点没有左子结点，只有一个右子结点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        最直接的解法，先中序遍历得到list，再遍历list生成要求的树，效率贼低。。。
        TODO：高效的解法暂时没看懂，待补充
        """

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            val.append(root.val)
            dfs(root.right)
            return root

        def generate(new_root, index):
            if index >= len(val):
                return
            new_root.right = TreeNode(val[index])
            new_root = new_root.right
            generate(new_root, index + 1)
            return new_root

        if not root:
            return
        val = []
        dfs(root)
        new_root = TreeNode(val[0])
        generate(new_root, 1)
        return new_root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(1)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)
    solution = Solution()
    res = solution.increasingBST(root)
    print(res)
