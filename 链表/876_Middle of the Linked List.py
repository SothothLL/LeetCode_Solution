# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head.next
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is None:
            return slow
        return slow.next


"""
给定一个带有头结点head的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

快慢指针，快指针行进步长为慢指针两倍，当快指针到达链表尾部时，慢指针正好在链表中间。
"""