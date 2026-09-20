"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldToCopy = {None: None}

        # First pass:
        # Create a copy of every original node.
        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # Second pass:
        # Connect the copied nodes using next and random.
        cur = head

        while cur:
            copy = oldToCopy[cur]

            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]

            cur = cur.next

        return oldToCopy[head]

        #{
   # None: None,
   # A: A_copy,
   # B: B_copy,
   # C: C_copy
#}