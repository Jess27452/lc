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
    def reorderList(self, head: Optional[ListNode]) -> None:
        # An empty list or one-node list is already reordered.
        if not head or not head.next:
            return

        # -------------------------------------------------
        # Step 1: Find the middle of the linked list
        # -------------------------------------------------

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # For 1 → 2 → 3 → 4 → 5:
        # slow points to node 3.
        #
        # For 1 → 2 → 3 → 4:
        # slow points to node 2.

        # -------------------------------------------------
        # Step 2: Separate and reverse the second half
        # -------------------------------------------------

        second = slow.next

        # Disconnect the first half from the second half.
        slow.next = None

        previous = None

        while second:
            # Save the next node before changing second.next.
            temporary = second.next

            # Reverse the arrow.
            second.next = previous

            # Move previous forward.
            previous = second

            # Move second forward using the saved node.
            second = temporary

        # previous is now the head of the reversed second half.

        # -------------------------------------------------
        # Step 3: Merge the two halves
        # -------------------------------------------------

        first = head
        second = previous

        while second:
            # Save where each pointer needs to go next.
            first_next = first.next
            second_next = second.next

            # Connect one node from the first half
            # to one node from the reversed second half.
            first.next = second
            second.next = first_next

            # Move both pointers forward.
            first = first_next
            second = second_next     