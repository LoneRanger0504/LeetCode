"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        先判断链表中是否有环，如果有环，则从快慢指针相遇的位置开始，
        从链表首端使用一个新的指针和慢指针同步走，slow 和 new 没相遇就一直走，
        两个指针相遇的位置就是链表环的入口
        注意这里三个指针都从哑结点开始，最后返回环的入口不需要dummy.next
        """
        dummy = ListNode(0)
        dummy.next = head
        hasCycle = False
        fast = dummy
        slow = dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if not hasCycle:
            return
        new = dummy
        while slow != new:
            slow = slow.next
            new = new.next
        return new
