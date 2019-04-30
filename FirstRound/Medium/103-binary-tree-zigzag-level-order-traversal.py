# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        使用两个栈模拟锯齿形层次遍历。先把root加到stack1,取出root后，将root的子树按照先左后右的顺序压到stack2，这样第二层出栈就是从右到左遍历
        接着再对stack2元素出栈，按照从右到左的顺序压到stack1中，这样第三层出栈的时候就是从左到右遍历，实现锯齿形层次遍历
        
        """
        res = []
        if not root:
            return res
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1 or stack2:
            size1 = len(stack1)
            temp1 = []
            temp2 = []
            while size1 > 0:
                root = stack1.pop()
                size1 -= 1
                temp1.append(root.val)
                #  按照从左到右的顺序压到stack2
                if root.left:
                    stack2.append(root.left)
                if root.right:
                    stack2.append(root.right)
            if len(temp1) > 0:
                res.append(temp1)
            size2 = len(stack2)
            while size2 > 0:
                root = stack2.pop()
                size2 -= 1
                temp2.append(root.val)
                #  按照从右到左的顺序压到stack1
                if root.right:
                    stack1.append(root.right)
                if root.left:
                    stack1.append(root.left)
            if len(temp2) > 0:
                res.append(temp2)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(5)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.zigzagLevelOrder(root)
    print(res)
