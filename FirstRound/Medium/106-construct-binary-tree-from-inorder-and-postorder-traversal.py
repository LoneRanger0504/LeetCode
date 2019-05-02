"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type postorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """
        利用递归，每次在后序列表中找到root，根据root在中序遍历中划分左右子树
        左子树为inorder[:root_index]，postorder[:root_index]
        右子树为inorder[root_index + 1:], postorder[root_index:-1]
        递归
        """

        def buildTreeCore(inorder, postorder):
            if not inorder or not postorder:
                return
            if len(postorder) == 1:
                return TreeNode(postorder[-1])
            # 确定根节点
            root_val = postorder[-1]
            root = TreeNode(root_val)
            root.left = root.right = None

            root_index = inorder.index(root_val)
            root.left = buildTreeCore(inorder[:root_index], postorder[:root_index])
            root.right = buildTreeCore(inorder[root_index + 1:], postorder[root_index:-1])
            return root

        if not inorder or not postorder:
            return
        return buildTreeCore(inorder, postorder)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    solution = Solution()
    res = solution.buildTree(inorder, postorder)
    print(res)
