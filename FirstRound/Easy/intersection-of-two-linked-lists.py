# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
编写一个程序，找到两个单链表相交的起始节点。
注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        (1)用辅助栈，依次把两个链表的节点加到两个辅助栈中，从链表尾开始，依次弹出栈顶元素，判断是否相同，相同继续弹出比较下一个栈顶，找到最后一个相同节点
        时间复杂度O(m+n)
        (2)类似快慢指针，先遍历两个链表得到各自长度，计算长度差，然后长链表先走长度差步，再两个链表一起走，第一个相同节点就是第一个公共节点
        """

        def getListLength(head):
            length = 0
            node = head
            while node:
                length += 1
                node = node.next
            return length

        len_a = getListLength(headA)
        len_b = getListLength(headB)
        if len_a > len_b:
            diff = len_a - len_b
            Long = headA
            Short = headB
        else:
            diff = len_b - len_a
            Long = headB
            Short = headA
        for i in range(diff):
            Long = Long.next
        while Long and Short and Long != Short:
            Long = Long.next
            Short = Short.next
        res = Long
        return res


if __name__ == '__main__':
    A = ListNode(4)
    B = ListNode(5)
    A.next = ListNode(1)
    A.next.next = ListNode(8)
    A.next.next.next = ListNode(4)
    A.next.next.next.next = ListNode(5)
    B.next = ListNode(0)
    B.next.next = ListNode(1)
    B.next.next.next = ListNode(8)
    B.next.next.next.next = ListNode(4)
    B.next.next.next.next.next = ListNode(5)
    solution = Solution()
    res = solution.getIntersectionNode(A, B)
    print(res)
