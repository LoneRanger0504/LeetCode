# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return
        root = TreeNode(pre[0])
        root_index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:root_index + 1], tin[:root_index])
        root.right = self.reConstructBinaryTree(pre[root_index + 1:], tin[root_index + 1:])
        return root


if __name__ == '__main__':
    input_pre = [1, 2, 4, 7, 3, 5, 6, 8]
    input_tin = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    res = solution.reConstructBinaryTree(input_pre, input_tin)
    print(res)
