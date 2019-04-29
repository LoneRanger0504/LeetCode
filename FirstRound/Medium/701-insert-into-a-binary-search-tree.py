"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        """
        利用二叉搜索树的特点，根节点的值大于左子树的值，小于右子树的值
        递归查找插入位置，根据val与当前root.val的大小关系再判断是否是插入位置，是则插入，否则递归查找
        其实这里可以不用递归，因为肯定能找到一个插入位置，使用while进行循环迭代，每次更新root重新循环即可
        """
        if not root:
            return
        if val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(7)
    input_val = 5
    solution = Solution()
    res = solution.insertIntoBST(root, input_val)
    print(res)
