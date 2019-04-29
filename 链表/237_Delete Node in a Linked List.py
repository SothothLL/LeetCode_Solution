# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

链表删除节点一般是将待删除节点的前驱节点的后继变为删除节点的后继。函数的输入是删除的节点node，不是链表head，无法得到待删除节点的前
驱节点，因此直接将节点赋值为后继节点，并把节点的后继变为后继节点的后继。相当于复制了后继的值并删除了后继节点。
"""