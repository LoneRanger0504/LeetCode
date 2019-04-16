"""
返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

(回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，
对于 node.left 的任何后代，值总 < node.val，
而 node.right 的任何后代，值总 > node.val。
此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        """
        思路类似于先序和中序构造二叉树，只不过这里结合了二叉搜索树的特点，
        确定根节点后，小于根节点的值得到左子树的前序遍历，第一个元素为根节点
        大于根节点的值得到右子树的前序遍历，也是第一个值为根节点，
        递归
        """
        if not preorder:
            return
        root = TreeNode(preorder[0])
        left = []
        right = []
        for i in preorder[1:]:
            if i < root.val:
                left.append(i)
            else:
                right.append(i)
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root


if __name__ == '__main__':
    input_preorder = [8, 5, 1, 7, 10, 12]
    solution = Solution()
    res = solution.bstFromPreorder(input_preorder)
    print(res)
