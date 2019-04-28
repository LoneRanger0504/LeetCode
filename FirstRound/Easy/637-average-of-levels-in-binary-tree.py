"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        """
        还是借助队列实现非递归层次遍历(102题)，把每行的平均值添加到res中即可
        注意一下Python中的除法，如果直接使用 / ，得到的并不是带浮点数的正确平均值
        因为Python除法还分精确除法，可以选择导入精确除法，也可以在除数或者被除数外面套一个float函数
        这样就和其他语言一样，当运算符两边有浮点数时就采用浮点数运算
        """
        if not root:
            return
        queue = [root]
        res = []
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
            res.append((sum(temp)) / float(len(temp)))
        return res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    input_val = 5
    solution = Solution()
    res = solution.averageOfLevels(root)
    print(res)
