# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseList(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Empty linked list
        if not head:
            return None

        # If head is the last node, this stays as head.
        # Otherwise, recursion replaces it with the new head.
        new_head = head

        if head.next:
            # Reverse everything after the current node.
            new_head = self.reverseList(head.next)

            # Make the next node point backward to head.
            head.next.next = head

        # Remove the original forward connection.
        head.next = None

        return new_head
        #The time is O(n) because each node is processed once.

#The extra space is O(n) because recursion creates one function call on the call stack for each node.