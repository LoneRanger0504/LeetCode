"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素
"""


# Definition
# for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """
        思路同106，在先序序列中找到第一个节点作为root，在中序序列中划分新的左右子树
        递归生成
        """

        def buildTreeCore(inorder, postorder):
            if not inorder or not postorder:
                return
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            # 确定根节点
            root_val = inorder[0]
            root = TreeNode(root_val)
            root.left = root.right = None

            root_index = postorder.index(root_val)
            root.left = buildTreeCore(inorder[1:root_index + 1], postorder[:root_index])
            root.right = buildTreeCore(inorder[root_index + 1:], postorder[root_index + 1:])
            return root

        if not inorder or not postorder:
            return
        return buildTreeCore(inorder, postorder)


if __name__ == '__main__':
    inorder = [1, 2]
    postorder = [2, 1]
    solution = Solution()
    res = solution.buildTree(inorder, postorder)
    print(res)
