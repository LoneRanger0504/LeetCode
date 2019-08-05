# -*- coding: utf-8 -*-
# @Author  : Lone Ranger
# @Function :


"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        #  1.复制原有链表
        def clone_listnode(head):
            node = head
            while node:
                cloned = RandomListNode(node.label)
                cloned.next = node.next
                node.next = cloned
                node = cloned.next

        #  2.复制随机指针
        def clone_random(head):
            node = head
            while node:
                cloned = node.next
                if node.random:
                    cloned.random = node.random.next
                node = cloned.next

        #  3.拆分两个链表
        def reconnect(head):
            node = head
            res = None
            cloned = None
            if node:
                res = cloned = node.next
                node.next = cloned.next
                node = node.next
            while node:
                cloned.next = node.next
                cloned = cloned.next
                node.next = cloned.next
                node = node.next
            return res

        clone_listnode(pHead)
        clone_random(pHead)
        res = reconnect(pHead)
        return res


if __name__ == '__main__':
    C = RandomListNode(1)
    B = RandomListNode(2)
    A = RandomListNode(3)
    A.next = B
    A.random = C
    B.next = C
    C.random = B
    solution = Solution()
    res = solution.Clone(A)
    print(res)
