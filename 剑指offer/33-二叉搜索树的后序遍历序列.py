# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        index = 0
        for i in range(len(sequence)):
            if sequence[i] < root:
                index += 1
            else:
                break
        for j in range(index, len(sequence)):
            if sequence[j] < root:
                return False

        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[index + 1:])
        return left and right


if __name__ == '__main__':
    input_sequence = [5, 7, 6, 9, 11, 10, 8]
    solution = Solution()
    res = solution.VerifySquenceOfBST(input_sequence)
    print(res)
