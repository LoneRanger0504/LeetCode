"""
给定一个 N 叉树，返回其节点值的前序遍历。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        (1)递归版本就是直接dfs
        (2)非递归版本使用队列辅助，注意有两个小细节，
        为了实现前序遍历，添加节点到队列中时，从children数组从后往前添加，
        然后在pop的时候，使用queue.pop(-1)这样取出来的是队列的最后一个元素，
        从而实现了前序遍历
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            node = queue[-1]
            res.append(node.val)
            queue.pop(-1)
            for child in node.children[::-1]:
                queue.append(child)
        return res
