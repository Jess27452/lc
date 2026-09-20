# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


# Definition for a singly linked-list node.
class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None
    ):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node comes before the actual answer.
        # It makes building the result list easier.
        dummy = ListNode()

        # cur always points to the last node
        # currently in the answer list.
        cur = dummy

        # Carry from the previous addition.
        carry = 0

        # Continue while:
        # 1. l1 still has a digit, or
        # 2. l2 still has a digit, or
        # 3. there is a remaining carry.
        while l1 or l2 or carry:

            # Get the current digit from l1.
            # If l1 is finished, use 0.
            v1 = l1.val if l1 else 0

            # Get the current digit from l2.
            # If l2 is finished, use 0.
            v2 = l2.val if l2 else 0

            # Add the two digits and the previous carry.
            total = v1 + v2 + carry

            # Calculate the carry for the next position.
            carry = total // 10

            # Current answer digit.
            digit = total % 10

            # Create a new answer node.
            cur.next = ListNode(digit)

            # Move cur to the new last node.
            cur = cur.next

            # Move l1 forward when it still exists.
            l1 = l1.next if l1 else None

            # Move l2 forward when it still exists.
            l2 = l2.next if l2 else None

        # Skip the dummy node and return the real answer.
        return dummy.next      