"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        使用快慢指针，快指针一次走两步，慢指针一次走一步，快指针走到链表尾，慢指针走到中间节点
        :param head:
        :return:
        """
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
