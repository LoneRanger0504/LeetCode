"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        核心思想在于快慢指针，找到旋转之后的头节点和尾节点
        先遍历统计链表长度，再将k取模，快指针先走k步，再快慢指针一起走
        快指针走到尾时，慢指针的next就是新的头结点，从慢指针处断开
        """
        if not head or k == 0:
            return head
        head_len = 0
        temp = head
        while temp:
            head_len += 1
            temp = temp.next
        k = k % head_len
        if k == 0:
            return head
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        res = slow.next
        fast.next = head
        slow.next = None
        return res


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    k = 2
    solution = Solution()
    res = solution.rotateRight(head, k)
    while res:
        print(res.val)
        res = res.next
