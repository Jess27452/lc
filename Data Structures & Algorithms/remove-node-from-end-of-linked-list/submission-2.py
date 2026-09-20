#from video
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:#make the gap between left and right pointer as n
        #for exampels n=2, n-1,one step, n- anotehr step
        #so at the end it moves 2, n will be 0 at the ened but for n=0, we dont need
        #it to run further, so we set n>0
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next