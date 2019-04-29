# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """
        
        """
        if not nums:
            return
        max_index = nums.index(max(nums))
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root


if __name__ == '__main__':
    input_list = [3, 2, 1, 6, 0, 5]
    solution = Solution()
    res = solution.constructMaximumBinaryTree(input_list)
    print(res)
