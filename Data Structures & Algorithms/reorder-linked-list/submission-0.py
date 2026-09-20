# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head) -> None:
        if not head or not head.next:
            return

        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next#slow moves one step

#fast moves two steps
#So we need to repeatedly take:

#the next node from the front

#the next node from the back

#But a singly linked list only lets us move forward, never backward.

        # 2. Reverse second half
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # 3. Merge alternating
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2