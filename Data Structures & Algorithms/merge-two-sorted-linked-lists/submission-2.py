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
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node makes it easier to build the new list.
        dummy = ListNode()

        # tail always points to the last node
        # in the merged linked list.
        tail = dummy

        # Continue while both lists still have nodes.
        while list1 and list2:

            # Choose the smaller current node.
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            # Move tail to the node we just added.
            tail = tail.next

        # At this point, at least one list is empty.
        # Attach the remaining part of the other list.
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # dummy itself is not part of the answer.
        return dummy.next  