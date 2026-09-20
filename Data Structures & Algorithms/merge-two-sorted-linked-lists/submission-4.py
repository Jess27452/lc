# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # If either list is empty, return the other list.
        if not list1:
            return list2

        if not list2:
            return list1

        # Choose the first node of the merged list.
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        # tail starts at the first result node.
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Attach the remaining nodes.
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return head