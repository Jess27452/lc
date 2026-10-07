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
        next: Optional[ListNode] = None
    ):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Both pointers begin at the first node.
        slow = head
        fast = head

        # fast must exist, and fast.next must exist,
        # because fast moves two steps at a time.
        while fast and fast.next:
            # Slow moves one node.
            slow = slow.next

            # Fast moves two nodes.
            fast = fast.next.next

            # If they point to the same node,
            # there must be a cycle.
            if slow == fast:
                return True

        # If fast reaches None, the list has an ending,
        # so there is no cycle.
        return False