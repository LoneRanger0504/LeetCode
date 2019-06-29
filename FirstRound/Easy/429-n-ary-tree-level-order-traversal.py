"""
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        """
        与二叉树的层次遍历唯一的区别在于，二叉树是判断有没有左右子树
        n叉树是遍历子节点所在的list，从而将节点加到队列中
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                root = queue.pop(0)
                temp.append(root.val)
                size -= 1
                #  与二叉树的区别就在这里
                for i in root.children:
                    queue.append(i)
            res.append(temp)
        return res
