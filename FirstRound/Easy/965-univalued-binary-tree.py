"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        思路很直观，只要找到一个不相同的值即返回False.
        (1)递归做法就是使用一个set去重，dfs递归遍历，最后判断set是否只含一个元素，
        缺点就是需要全部遍历完再判断
        (2)非递归就是使用一个队列进行广度优先遍历，只要遇到与root值不相同的值就返回False
        """
        #  递归，借助一个set
        # def dfs(root):
        #     if not root:
        #         return
        #     val_set.add(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        #     return root
        # if not root:
        #     return False
        # flag = True
        # val_set = set()
        # # val_set.add(root.val)
        # dfs(root)
        # return len(val_set) == 1
        #  BFS非递归
        queue = [root]
        val = root.val
        while queue:
            root = queue.pop()
            if root.val != val:
                return False
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(2)
    solution = Solution()
    res = solution.isUnivalTree(root)
    print(res)
