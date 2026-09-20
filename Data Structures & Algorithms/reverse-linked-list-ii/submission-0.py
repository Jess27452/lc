# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None
    ):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        # Dummy is placed before head.
        # It helps when left == 1.
        dummy = ListNode(0, head)

        # left_prev will stop at the node before position left.
        # cur will stop at the node at position left.
        left_prev = dummy
        cur = head

        for _ in range(left - 1):
            left_prev = cur
            cur = cur.next

        # Save the original first node of the section.
        # After reversal, it becomes the last node.
        left_node = cur

        # Reverse exactly right - left + 1 nodes.
        prev = None

        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Reconnect the reversed section.

        # Original left node is now the end of the reversed section.
        left_node.next = cur

        # Node before left should point to the new front,
        # which is the original right node.
        left_prev.next = prev

        return dummy.next