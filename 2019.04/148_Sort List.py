# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        self.fastSort(head, None)
        return cur

    def swap(self, a: ListNode, b: ListNode):
        temp = a.val
        a.val = b.val
        b.val = temp

    def getSeparator(self, p_begin: ListNode, p_end:ListNode) -> ListNode:
        p = p_begin
        q = p_begin.next
        key = p.val
        while q != p_end:
            if q.val<key:
                p = p.next
                self.swap(p,q)
            q = q.next
        self.swap(p_begin, p)
        return p

    def fastSort(self, p_begin: ListNode, p_end:ListNode):
        if p_begin != p_end:
            separator = self.getSeparator(p_begin, p_end)
            self.fastSort(p_begin, separator)
            self.fastSort(separator.next, p_end)
