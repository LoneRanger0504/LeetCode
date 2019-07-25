# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        p_node = pHead
        p_prev = None
        res = None

        while p_node:
            # 先记录next
            p_next = p_node.next
            # 如果p_next为空表示到了链表尾部，这时候返回头结点，即当前的pNode
            if not p_next:
                res = p_node
            # 先令p_node.next = None
            p_node.next = p_prev
            # 更新p_prev和p_node
            p_prev = p_node
            p_node = p_next
        return res


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    res = solution.ReverseList(head)
    while res:
        print(res.val)
        res = res.next
