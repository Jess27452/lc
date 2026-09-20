# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
#groupPrev means the node right before the group we want to reverse
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            #the next lememht of this reverse group

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev# make the first one point to the kth.next, which
                # is the head of next group
                prev = curr#make the prev become sthe current one, so the next one can [oitn to the 
                #current one]
                curr = tmp

            tmp = groupPrev.next #Before changing groupPrev.next, remember old start:
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr