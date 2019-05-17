# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        主要考虑进位问题，从末位开始相加，对应位置的值为(l1.val+l2.val+carry) % 10,对应的进位值为(l1.val+l2.val+carry) / 10
        生成链表节点。注意直到l1和l2都为空，注意最后还需要判断一下进位是否为1，是否需要新增一个节点
        """
        dummy = ListNode(0)
        p = l1
        q = l2
        carry = 0
        head = dummy
        while p or q:
            p_val = p.val if p else 0
            q_val = q.val if q else 0
            sum = p_val + q_val + carry
            carry = sum / 10
            head.next = ListNode(sum % 10)
            head = head.next
            if p:
                p = p.next
            if q:
                q = q.next
        if carry == 1:
            head.next = ListNode(1)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solution = Solution()
    res = solution.addTwoNumbers(l1, l2)
    print(res)
