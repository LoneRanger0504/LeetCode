# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :二叉树的最大深度

"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        (1)递归解法1，返回左右子树的最大深度+1
        (2)递归解法2
        (3)非递归解法，使用栈来实现层次遍历，每遍历一层，depth+1
        """
        #  (1)递归解法1
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        #  (2)递归解法2
        # def countDepth(root, max_depth, depth):
        #     if not root:
        #         return max(max_depth, depth)
        #     max_depth = countDepth(root.left, max_depth, depth+1)
        #     max_depth = countDepth(root.right, max_depth, depth+1)
        #     return max_depth
        # if not root:
        #     return 0
        # max_depth = 1
        # depth = 0
        # return countDepth(root, max_depth, depth)

        #  (3)非递归解法，使用辅助栈对二叉树进行层次遍历，每次将每一层的子节点加到new_stack中，并更新为stack，每遍历完一层，depth+1
        #  直到stack为空，表示遍历到了最后一层的叶子节点，最后返回层数，也就是树的高度
        stack = [root]
        depth = 0
        while stack:
            new_stack = []
            for node in stack:
                if node.left != None:
                    new_stack.append(node.left)
                if node.right != None:
                    new_stack.append(node.right)
            depth += 1
            stack = new_stack
        return depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.maxDepth(root)
    print(res)
