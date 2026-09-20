# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Because we moved fast n steps ahead, the distance between fast and slow is always n.
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
        #We keep a pointer to the first node (the head) because after modifying the list we still need a way to return the beginning of the list. In a linked list, the only way to access the entire structure is through its first node. If you lose that pointer, you lose access to the list.