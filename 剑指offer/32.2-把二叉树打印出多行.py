# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        res = []
        if not pRoot:
            return res
        queue = [pRoot]
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                root = queue.pop(0)
                temp.append(root.val)
                size -= 1
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(temp)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    solution = Solution()
    res = solution.Print(root)
    print(res)
