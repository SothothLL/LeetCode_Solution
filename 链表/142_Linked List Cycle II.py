# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        cycle_node = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                cycle_node = True
                break
        if cycle_node:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
        return None


"""
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始）。如果pos是-1，则在该链表中没有环。

先用快慢指针判断链表是否有环，如果存在，则慢指针行走步数为环外长度a+环内行走x，快指针行走步数为环外长度a+环长度b+环内行走x，又因为
快指针步长是慢指针的2倍，因此a=b-x，所以当慢指针再走a步即回到环头，那么设置一个新指针从链表头行走a步长度即为环头。
"""