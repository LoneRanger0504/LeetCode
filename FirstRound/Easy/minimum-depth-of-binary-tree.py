# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function : 二叉树的最小高度

"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        (1)深度优先遍历DFS：根节点为空，返回0，不为空：从根节点出发，依次递归计算左右子树的高度，返回左右子树高度的最小值+1
        (2)广度优先遍历BFS：借助队列实现广度优先搜索,只要找到一个左右子节点都为空的，直接返回当前的树的深度
        """
        #  (1)DFS
        # if not root:
        #     return 0
        #
        # left_depth = self.minDepth(root.left)
        # right_depth = self.minDepth(root.right)
        #
        # if not root.left:
        #     return 1 + right_depth
        # if not root.right:
        #     return 1 + left_depth
        #
        # return 1 + min(left_depth, right_depth)

        #  (2)BFS
        import collections
        if not root:
            return 0

        queue = collections.deque()
        queue.append(root)
        min_level = 0
        while queue:
            level_size = len(queue)
            min_level += 1

            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return min_level

        return min_level


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.minDepth(root)
    print(res)
