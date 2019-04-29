"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        (1)前序深度优先搜索，使用一个辅助字典，把每一层的层数作为key，对应的value就是该层对应的节点值列表
        如果层数不在字典键中，新建一个list并将对应的值加进去，如果已经存在，将当前节点的值追加到对应的value中
        最后按照键获取所有的list，即实现层次遍历
        (2)层次遍历，每次遍历一层的时候，先获取到这一层的节点个数，创建一个temp用于保存当前层的所有值
        然后依次取出队列的第一个，注意这里queue.pop(0)表示取出第一个，如果是-1就是取出最后一个，二叉树的右视图就是使用这一特点
        然后就是将节点值追加到temp，中，当前层节点数减1，
        当size=0表示当前层遍历完毕，此时已经由内层while循环中的append将下一层的所有节点添加到队列了，直到队列为空完成层次遍历
        """
        #  递归解法，借助辅助字典
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
        # return [dic.get(i) for i in dic.keys()]
        #  层序遍历，使用队列
        if not root:
            return
        res = []
        queue = [root]
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
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    res = solution.levelOrder(root)
    print(res)
