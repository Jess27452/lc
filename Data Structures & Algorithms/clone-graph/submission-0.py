"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # ---------------------------------------------------
        # WHAT DOES node: 'Node' MEAN?
        # ---------------------------------------------------
        # It is a TYPE HINT.
        #
        # node: 'Node'
        # means:
        #   "the input parameter node is supposed to be a Node object"
        #
        # -> 'Node'
        # means:
        #   "this function is supposed to return a Node object"
        #
        # The quotes do NOT mean the input is a string.
        # The actual input is still a real Node object.
        #
        # So this:
        #   def cloneGraph(self, node: 'Node') -> 'Node':
        #
        # really means:
        #   input: a Node
        #   output: a Node
        #
        # The quotes are just for the type hint syntax.

        # ---------------------------------------------------
        # If the graph is empty, return None
        # ---------------------------------------------------
        # This is the only case where we return None:
        # there is no starting node at all.
        if not node:
            return None

        # ---------------------------------------------------
        # oldToNew dictionary
        # ---------------------------------------------------
        # Key   = original node
        # Value = cloned node
        #
        # Example:
        # oldToNew[original node 1] = cloned node 1
        #
        # Why do we need this?
        #
        # 1. To avoid cloning the same node many times
        # 2. To avoid infinite recursion in cycles
        # 3. To connect original neighbors to cloned neighbors correctly
        oldToNew = {}

        # ---------------------------------------------------
        # DFS function clones one node and all nodes reachable from it
        # ---------------------------------------------------
        def dfs(node):
            # -----------------------------------------------
            # If this node was already cloned before,
            # just return the clone from the dictionary
            # -----------------------------------------------
            # This prevents infinite loops in graphs like:
            # 1 -- 2
            # where 2 points back to 1
            if node in oldToNew:
                return oldToNew[node]

            # -----------------------------------------------
            # Create a clone of the current node
            # -----------------------------------------------
            # It has the same value as the original node
            # but it is a completely new object in memory
            copy = Node(node.val)

            # -----------------------------------------------
            # Save the mapping IMMEDIATELY
            # -----------------------------------------------
            # This is very important.
            #
            # We store it before exploring neighbors so that
            # if the graph comes back to this node through a cycle,
            # we can immediately return the clone instead of cloning again.
            oldToNew[node] = copy

            # -----------------------------------------------
            # Clone all neighbors
            # -----------------------------------------------
            # For each original neighbor:
            # 1. recursively clone that neighbor
            # 2. append the cloned neighbor to copy.neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # -----------------------------------------------
            # What if this node has NO neighbors?
            # -----------------------------------------------
            # Then this loop runs zero times.
            #
            # That means copy.neighbors stays as []
            #
            # So the function still returns the cloned node,
            # just with an empty neighbor list.
            #
            # Example:
            # original node: val = 3, neighbors = []
            # cloned node:   val = 3, neighbors = []
            #
            # It does NOT return None in this case.
            return copy

        # ---------------------------------------------------
        # Start DFS from the given input node
        # ---------------------------------------------------
        # This returns the cloned version of the starting node,
        # and because DFS recursively clones neighbors,
        # the whole graph gets copied.
        return dfs(node) 