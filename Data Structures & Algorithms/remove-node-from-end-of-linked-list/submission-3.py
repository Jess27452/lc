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
    def removeNthFromEnd(
        self,
        head: Optional[ListNode],
        n: int
    ) -> Optional[ListNode]:

        # Dummy is placed before the original head.
        dummy = ListNode(0, head)

        # left begins at dummy.
        # right begins at the real head.
        left = dummy
        right = head

        # Move right forward n nodes.
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers together.
        #
        # When right reaches None,
        # left will be immediately before the node
        # we want to delete.
        while right:
            left = left.next
            right = right.next

        # Skip the target node.
        left.next = left.next.next

        # Return the real head, skipping dummy.
        return dummy.next 