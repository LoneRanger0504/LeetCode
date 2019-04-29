"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        核心思路同102题层次遍历
        (1)前序dfs得到每层的list,最后取每层的最后一个元素
        (2)使用队列进行BFS，把每层的最后一个元素加到res中，判断依据就是每层的size==0
        """
        #  (1)前序DFS
        # def dfs(root, level):
        #     if not root:
        #         return
        #     if level in dic.keys():
        #         dic.get(level).append(root.val)
        #     else:
        #         dic[level] = [root.val]
        #     dfs(root.left, level+1)
        #     dfs(root.right, level+1)
        #     return root
        # dic = {}
        # res = []
        # if not root:
        #     return res
        # dfs(root, 1)
        # return [dic.get(i)[-1] for i in dic.keys()]
        #  (2)非递归：使用队列添加每行的最后一个元素
        if not root:
            return
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            while size > 0:
                root = queue.pop(0)
                size -= 1
                if size == 0:
                    res.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    input_val = 5
    solution = Solution()
    res = solution.rightSideView(root)
    print(res)
