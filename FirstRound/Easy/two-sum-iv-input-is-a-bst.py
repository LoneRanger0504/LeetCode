"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        """
        几种思路：
        (1)利用二叉搜索树的性质，递归中序遍历，得到一个节点值升序排列的list，再按照167题的双指针思路遍历，
        需要注意list有可能只有一个根节点，这种情况return False
        (2)使用一个辅助栈实现层次遍历(BFS)
        每次把每层的节点取出来，判断target-node.val是否在list中，在就返回True,不在就把val加入list
        (3)类似第一题，使用hash表存储节点，一次hash,判断target-node.val是否在hash表中
        """
        #  (1)中序遍历+双指针
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     traversal_list.append(root.val)
        #     dfs(root.right)
        # traversal_list = []
        # if not root :
        #     return False
        # dfs(root)
        # start = 0
        # end = len(traversal_list) - 1
        # if start == end:
        #     return False
        # while start < end:
        #     num = traversal_list[start] + traversal_list[end]
        #     if num == k:
        #         return True
        #     elif num > k:
        #         end -= 1
        #     else:
        #         start += 1
        # return False
        #  (2)辅助栈
        if not root:
            return False
        queue = [root]
        val_list = [root.val]
        while queue:
            node = queue.pop(0)
            if node.left:
                if k - node.left.val in val_list:
                    return True
                else:
                    queue.append(node.left)
                    val_list.append(node.left.val)
            if node.right:
                if k - node.right.val in val_list:
                    return True
                else:
                    queue.append(node.right)
                    val_list.append(node.right.val)
        return False


if __name__ == '__main__':
    root = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    res = solution.findTarget(root, 6)
    print(res)
