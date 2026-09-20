# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None
    ):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        # No linked lists were given.
        if not lists:
            return None

        # Keep merging pairs until one list remains.
        while len(lists) > 1:
            merged_lists = []

            # Take two lists at a time.
            for i in range(0, len(lists), 2):
                list1 = lists[i]

                # There may not be a second list
                # when the number of lists is odd.
                list2 = (
                    lists[i + 1]
                    if i + 1 < len(lists)
                    else None
                )

                merged = self.mergeTwoLists(list1, list2)
                merged_lists.append(merged)

            # Use the newly merged lists in the next round.
            lists = merged_lists

        # Only one merged list remains.
        return lists[0]

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # At least one list is now empty.
        # Attach the remaining non-empty list.
        tail.next = list1 if list1 else list2

        return dummy.next