# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        """
        :param listNode:
        :return:
        """
        """
        (1)先正向遍历添加到list，逆序输出list
        (2)栈/递归
        """
        # res = []
        # if not ListNode:
        #     return res
        # dummy = ListNode(0)
        # dummy.next = listNode
        # while dummy.next:
        #     res.append(dummy.next.val)
        #     dummy = dummy.next
        # return res[::-1]
        if not listNode:
            return []
        res = []

        def recuesive(head):
            if head.next:
                recuesive(head.next)
            res.append(head.val)

        recuesive(listNode)
        return res


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution()
    res = solution.printListFromTailToHead(head)
    print(res)
