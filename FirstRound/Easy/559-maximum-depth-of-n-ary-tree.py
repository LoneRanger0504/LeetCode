# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        """
        (1)非递归实现:使用队列辅助实现层次遍历，每次在进入新的一层时level加1即可
        (2)递归实现：使用dfs
        """
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            level += 1
            size = len(queue)
            while size > 0:
                root = queue.pop(0)
                size -= 1
                for child in root.children:
                    queue.append(child)
        return level
