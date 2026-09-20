"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #the reason we want to have NOn:None is because after we set cur=cur.next
        # and then we make cur becomes None
        #copy.next = oldToCopy[cur.next] useful for this line
        oldToCopy={None : None}
        cur = head
        print(cur)
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur]=copy
            cur=cur.next
        cur=head
        #this loop helps to create connection
        while cur:
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random] # we use the current nodes ,
            #not coplied one as the key of hashmap
            #
            cur=cur.next
        return oldToCopy[head]
