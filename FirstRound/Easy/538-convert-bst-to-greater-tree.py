# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        (1)比较蠢的办法，先中序遍历得到递增序列，依次累加，速度贼慢
        (2)可以直接在遍历的时候按照右子节点-根节点-左子节点的顺序遍历，把之前的值都累加起来即可
        """

        #  (1)低效做法
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     val.append(root.val)
        #     dfs(root.right)
        #     return root
        #
        # def changeTree(root):
        #     if not root:
        #         return
        #     changeTree(root.left)
        #     root.val += sum(val[val.index(root.val) + 1:])
        #     changeTree(root.right)
        #     return root
        #
        # if not root:
        #     return
        # val = []
        # dfs(root)
        # changeTree(root)
        # return root

        #  (2)一遍遍历,每次先将之前的值累加到root.val再更新新的val[0]
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val += val[0]
            val[0] = root.val
            dfs(root.left)
            return root

        if not root:
            return
        val = [0]
        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    solution = Solution()
    res = solution.convertBST(root)
    print(res)
