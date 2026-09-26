"""
import copy
# Definition for a Node.
class Node:, NoDefault
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        ot={}
        def dfs(node):
            if node in ot:
                return ot[node]
            copy=Node(node.val)
            ot[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
            

