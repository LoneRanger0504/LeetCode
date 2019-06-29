"""
给定一个 N 叉树，返回其节点值的后序遍历。
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        """
        (1)递归解法：深度优先搜索，唯一区别只在于获取下一个节点时是遍历children列表
        (2)非递归解法：使用队列，添加的时候从前往后添加，取的时候是从后往前
        将最后的结果数组反转
        """

        if not root:
            return
        res = []

        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)

        dfs(root)
        return res

        # if not root:
        #     return []
        # queue = [root]
        # res = []
        # while queue:
        #     node = queue.pop(-1)
        #     res.append(node.val)
        #     for child in node.children:
        #         queue.append(child)
        # return res[::-1]
