# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()# later reassign node

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2#expand node
                list2 = list2.next#list 2 去下一个
            node = node.next#node 去下一个

        node.next = list1 or list2#In Python, or does not return True/False necessarily. It returns one of the operands.
        #5 or 10     → 5
##0 or 10     → 10
#None or 7   → 7
#None or None → None
#Why?
#Because None is considered False in boolean context.
#So it returns the second value:None
#It doesn't return False. It returns the actual operand.

        return dummy.next