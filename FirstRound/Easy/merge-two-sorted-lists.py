"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        1.使用递归解法，递归地将较小的值添加到合并后的链表中。
        (1)首先判断l1 l2是否为空
        (2)将res指向首值较小的链表头，res.next指向新的两个链表中较小的值对应的链表头，递归直到结束
        2.循环解法
        使用哑结点
        遍历l1 l2直到某一个链表到达尾部，再将另外一个链表接在最后
        """
        # 递归：
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # if l1.val <= l2.val:
        #     res = l1
        #     res.next = self.mergeTwoLists(l1.next, l2)
        # else:
        #     res = l2
        #     res.next = self.mergeTwoLists(l1, l2.next)
        # return res
        # 循环
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next
        if l1 == None:
            cur.next = l2
        else:
            cur.next = l1
        return dummy.next
