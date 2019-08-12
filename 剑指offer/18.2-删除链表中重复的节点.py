# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        dummy = ListNode(0)
        dummy.next = pHead
        pre = dummy
        last = dummy.next
        while last:
            if last.next and last.val == last.next.val:
                while last.next and last.next.val == last.val:
                    last = last.next
                pre.next = last.next
                last = last.next
            else:
                pre = pre.next
                last = last.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    solution = Solution()
    res = solution.deleteDuplication(head)
    while res:
        print(res.val)
        res = res.next
