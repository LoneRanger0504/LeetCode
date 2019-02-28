"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        先使用一个哑结点指向head，避免繁琐的判断head是否为空
        使用快慢指针，都从dummy开始，当快指针的下个节点和下下个节点都不为空时，快指针走两步，慢指针走一步。
        如果在中途两指针相遇，则存在环，如果直到快指针走到最后一个节点都没有相遇，则不存在环
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
