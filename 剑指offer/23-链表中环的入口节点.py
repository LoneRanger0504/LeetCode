# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code herehua
        if not pHead:
            return
        dummy = ListNode(0)
        dummy.next = pHead
        hasCycle = False
        fast = dummy
        slow = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        head = dummy
        if hasCycle:
            while slow != head:
                slow = slow.next
                head = head.next
            return slow
        return
