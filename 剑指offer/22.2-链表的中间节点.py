# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # if head == None:
        #     return None
        # if head.next == None:
        #     return head
        # if head.next.next == None:
        #     return head.next
        # fast = head
        # slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # return slow
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    res = solution.middleNode(head)
    print(res.val)
