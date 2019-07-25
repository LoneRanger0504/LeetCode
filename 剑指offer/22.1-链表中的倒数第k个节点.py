# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        """
        :param head:
        :param k:
        :return:
        """
        """
        快慢指针，确保快指针先走k步，再两个指针一起走，使用哑结点dummy辅助
        需要注意三个边界条件：链表为空;k=0;链表长度小于k
        """
        if not head or k == 0:
            return
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range(k):
            # 这里需要特别注意如果链表的长度本身小于k，走到链表尾却没走到k步，说明出现异常，直接return
            if fast.next:
                fast = fast.next
            else:
                return
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    res = solution.FindKthToTail(head, 5)
    print(res)
