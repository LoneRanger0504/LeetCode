# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val >= pHead2.val:
            res = pHead2
            res.next = self.Merge(pHead1, pHead2.next)
        else:
            res = pHead1
            res.next = self.Merge(pHead1.next, pHead2)
        return res


if __name__ == '__main__':
    phead1 = ListNode(1)
    phead1.next = ListNode(3)
    phead1.next.next = ListNode(5)
    phead2 = ListNode(2)
    phead2.next = ListNode(4)
    phead2.next.next = ListNode(6)
    solution = Solution()
    res = solution.Merge(phead1, phead2)
    while res:
        print(res.val)
        res = res.next
