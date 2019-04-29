# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = [None]
        while head:
            stack.append(head)
            head = head.next
        rev = stack.pop()
        head = rev
        while head:
            head.next = stack.pop()
            head = head.next
        return rev


"""
反转一个单链表。

用一个栈来存储单链表的元素，再将元素依次从栈取出。
"""