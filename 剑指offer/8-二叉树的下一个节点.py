# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return
        res = None
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            res = pRight
        elif pNode.next:
            pCurrent = pNode
            pParent = pNode.next
            while pParent and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pParent.next
            res = pParent
        return res


if __name__ == '__main__':
    root = TreeLinkNode(5)
    root.left = TreeLinkNode(4)
    root.left.next = root
    root.left.left = TreeLinkNode(3)
    root.left.left.next = root.left
    root.left.right = TreeLinkNode(2)
    root.left.right.next = root.left
    solution = Solution()
    res = solution.GetNext(root.left.right)
    print(res)
