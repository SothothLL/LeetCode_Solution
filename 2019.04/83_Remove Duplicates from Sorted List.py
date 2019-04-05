# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head.next = Solution.deleteDuplicates(self, head.next)
        if head.val == head.next.val:
            head = head.next
        return head
