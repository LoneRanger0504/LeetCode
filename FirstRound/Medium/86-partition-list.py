"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        """
        使用两个链表分别记录大于x小于x的节点。
        得到两个链表，再将这两个链表接起来
        """
        if not head:
            return
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        temp = head
        head1 = dummy1
        head2 = dummy2
        while temp:
            if temp.val < x:
                head1.next = temp
                head1 = head1.next
            else:
                head2.next = temp
                head2 = head2.next
            temp = temp.next
        head1.next = dummy2.next
        head2.next = None
        return dummy1.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    solution = Solution()
    res = solution.partition(head, 3)
    while res:
        print(res.val)
        res = res.next
