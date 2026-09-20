# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0

        # push head of each list
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        tail.next = None
        return dummy.next     