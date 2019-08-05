# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here

        def find_path(root, target, temp):
            if not root:
                return
            temp.append(root.val)
            is_leaf = not root.left and not root.right
            if sum(temp) == target and is_leaf:
                res.append(temp[:])
            if root.left:
                find_path(root.left, target, temp)
            if root.right:
                find_path(root.right, target, temp)
            temp.pop()

        res = []
        if not root:
            return res
        find_path(root, expectNumber, [])
        return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    input_target = 22
    solution = Solution()
    res = solution.FindPath(root, input_target)
    print(res)
