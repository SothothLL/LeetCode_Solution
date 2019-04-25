# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        return self.divide(head)

    def divide(self, head: ListNode):
        if head.next is None:
            return head
        fast, slow, temp = head, head, head
        while fast is not None and fast.next is not None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        left = self.divide(head)
        right = self.divide(slow)
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode):
        temp_node = ListNode(0)
        temp = temp_node
        while left is not None and right is not None:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left is not None:
            temp.next = left
        if right is not None:
            temp.next = right
        return temp_node.next
