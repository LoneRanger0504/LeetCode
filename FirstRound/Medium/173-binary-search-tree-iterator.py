"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。
注：
next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        """
        看到二叉搜索树就应该想到利用中序遍历获取递增数组，再根据递增序列做文章
        在init()中完成中序遍历，但是递归或者借助栈的空间复杂度都超过O(h)
        这里有一种叫做Morris遍历的方法，能够实现时间复杂度O(N)空间复杂度O(1)的二叉树遍历
        TODO:待补充Morris遍历原理
        得到递增序列之后只需要根据题目要求实现next()和hasNext()即可
        """

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.val.append(root.val)
            dfs(root.right)
            return root

        self.val = []
        dfs(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        next_val = self.val.pop(0)
        return next_val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.val) > 0


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    instructors = ["next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    obj = BSTIterator(root)
    print(obj.hasNext())
    print(obj.next())
