# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        carry=0
        while l1 or l2 or carry:# reason that need or carry is 
        #Even after both linked lists are exhausted, there might 
        #still be a leftover carry (like the leading 1 in 18, 100, 1000, etc.) that needs to become a new node in the answer.
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            val=v1+v2+carry
            carry=val//10
            val=val%10
            cur.next=ListNode(val)
            
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next# since the output is also reversed