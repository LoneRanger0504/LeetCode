"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。
"""


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def cloneNode(head):
            """
            复制原有链表节点的val和next
            遍历head，新建一个cloned节点。把cur_node节点的val和next复制，random暂时不管，置为None
            复制后，cloned.next = cur_node.next即复制节点的next指向原节点的next
            再将当前节点更新为cloned.next即原来的第二个节点，完成复制
            :param head:
            :return:
            """
            cur_node = head
            while cur_node:
                cloned = Node(cur_node.val, cur_node.next, None)
                cur_node.next = cloned
                cur_node = cloned.next

        def cloneSibling(head):
            """
            功能：复制随机指针
            在已经复制完的链表上，依次把原节点的random复制给新节点
            先指向新节点，cloned = cur_node.next
            复制的逻辑为：新节点的random就是原节点的random.next
            复制完再指向原节点，即cur_node = cloned.next
            :param head:
            :return:
            """
            cur_node = head
            while cur_node:
                cloned = cur_node.next
                if cur_node.random:
                    cloned.random = cur_node.random.next
                cur_node = cloned.next

        def reconnect(head):
            """
            功能：把完成前两步复制的节点拆开，奇数位置上是原来的链表，偶数位置上经过复制的链表
            创建clonedhead和clonednode都指向总链表的head.next,也就是A`
            对当前节点，也就是总链表的头节点，cur_node.next = cur.next.next，即指向第三个节点
            再更新cur_node为第三个节点。此时cur_node指向第三个节点，clonednode指向第二个节点
            当cur_node不为空时，遍历。交替更新cur_node与clonednode
            先将clonednode.next指向cur_node.next即第二个节点的next指向第四个节点，再指向第四个节点
            再来更新cur_node.next=clonednode.next，也就是第三个节点的next指向第五个节点
            最后更新cur_node，指向第五个节点，循环依次遍历，完成链表拆分
            最后返回clonedhead,即返回复制链表的深拷贝
            :param head:
            :return:
            """
            cur_node = head
            clonedhead = None
            clonednode = None
            if cur_node:
                clonedhead = clonednode = cur_node.next
                cur_node.next = clonedhead.next
                cur_node = cur_node.next
            while cur_node:
                clonednode.next = cur_node.next
                clonednode = clonednode.next
                cur_node.next = clonednode.next
                cur_node = cur_node.next
            return clonedhead

        cloneNode(head)
        cloneSibling(head)
        return reconnect(head)


if __name__ == '__main__':
    node2 = Node(2, None, None)
    node1 = Node(1, node2, node2)
    node2.random = node2
    solution = Solution()
    res = solution.copyRandomList(node1)
    print(res)
