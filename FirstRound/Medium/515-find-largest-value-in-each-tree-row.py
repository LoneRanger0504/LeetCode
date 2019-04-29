"""
您需要在二叉树的每一行中找到最大的值。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        还是层序遍历，找到每一层的最大值即可，
        注意这里可以选择使用一个初始化的负无穷大，其实也可以初始化为每层的第一个节点值
        """

        #  (1)非递归
        # if not root:
        #     return
        # queue = [root]
        # res = []
        # while queue:
        #     size = len(queue)
        #     max_val = float('-inf')
        #     while size > 0:
        #         root = queue.pop(0)
        #         size -= 1
        #         if root.val > max_val:
        #             max_val = root.val
        #         if root.left:
        #             queue.append(root.left)
        #         if root.right:
        #             queue.append(root.right)
        #     res.append(max_val)
        # return res
        #  (2)递归
        def dfs(root, level):
            if not root:
                return
            if level in dic.keys():
                if root.val > dic.get(level):
                    dic[level] = root.val
            else:
                dic[level] = root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return root

        res = []
        if not root:
            return res
        dic = {}
        dfs(root, 1)
        return [dic[level] for level in dic.keys()]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    solution = Solution()
    res = solution.largestValues(root)
    print(res)
