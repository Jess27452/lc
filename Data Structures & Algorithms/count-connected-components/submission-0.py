from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # --------------------------------------------------------
        # par[i] = parent of node i
        #
        # At the beginning, every node is its own parent.
        # That means every node starts as its own separate group.
        #
        # Example for n = 5:
        # par = [0, 1, 2, 3, 4]
        #
        # This means:
        # 0 is root of its own set
        # 1 is root of its own set
        # 2 is root of its own set
        # 3 is root of its own set
        # 4 is root of its own set
        # --------------------------------------------------------
        par = [i for i in range(n)]

        # --------------------------------------------------------
        # rank[i] in THIS code is acting like the SIZE of the set
        # whose root is i.
        #
        # Initially every node is alone, so every set has size 1.
        #
        # Example:
        # rank = [1, 1, 1, 1, 1]
        # --------------------------------------------------------
        rank = [1] * n

        # --------------------------------------------------------
        # find(x):
        # returns the ROOT of the set containing x
        #
        # Why do we need this?
        # Because x itself may not be the root anymore.
        #
        # Example:
        # par = [0, 0, 0, 3, 3]
        #
        # Then:
        # find(2) should return 0
        # find(4) should return 3
        # --------------------------------------------------------
        def find(x: int) -> int:
            res = x

            # Keep moving upward until we reach a node
            # whose parent is itself.
            # That node is the root.
            while res != par[res]:
                # ------------------------------------------------
                # Path compression:
                # make this node jump closer to the root
                #
                # Example:
                # if res -> parent -> grandparent,
                # this line can make res point to grandparent.
                #
                # This helps keep future find() calls fast.
                # ------------------------------------------------
                par[res] = par[par[res]]
                res = par[res]

            return res

        # --------------------------------------------------------
        # union(a, b):
        # merge the sets containing a and b
        #
        # returns 1 if a merge happened
        # returns 0 if they were already in the same set
        # --------------------------------------------------------
        def union(a: int, b: int) -> int:
            p1 = find(a)   # root of a's set
            p2 = find(b)   # root of b's set

            # ----------------------------------------------------
            # If they already have the same root,
            # they are already in the same connected component.
            #
            # So there is no new merge.
            # ----------------------------------------------------
            if p1 == p2:
                return 0

            # ----------------------------------------------------
            # QUESTION YOU ASKED:
            # Why do we compare rank[p2] > rank[p1] ?
            #
            # Because we want to attach the SMALLER set
            # under the LARGER set.
            #
            # Why?
            # To keep the parent tree shallow.
            #
            # If the tree is shallow, find() is faster.
            #
            # If the tree becomes tall, find() has to walk
            # through many parent pointers.
            #
            # So:
            # - if set p2 is bigger, attach p1 under p2
            # - otherwise, attach p2 under p1
            #
            # This is called union by size / union by rank.
            # ----------------------------------------------------
            if rank[p2] > rank[p1]:
                # ------------------------------------------------
                # p2's set is bigger
                #
                # So make p2 the root of the merged set
                # by attaching p1 underneath p2
                # ------------------------------------------------
                par[p1] = p2

                # ------------------------------------------------
                # Now p2's set contains BOTH old sets,
                # so update its size:
                #
                # new size = old size of p2 + old size of p1
                # ------------------------------------------------
                rank[p2] += rank[p1]
            else:
                # ------------------------------------------------
                # p1's set is bigger, or they are equal size
                #
                # So make p1 the root of the merged set
                # by attaching p2 underneath p1
                # ------------------------------------------------
                par[p2] = p1

                # ------------------------------------------------
                # Now p1's set contains BOTH old sets,
                # so update its size
                # ------------------------------------------------
                rank[p1] += rank[p2]

            # A real merge happened
            return 1

        # --------------------------------------------------------
        # Start with n connected components,
        # because initially every node is alone
        # --------------------------------------------------------
        components = n

        # --------------------------------------------------------
        # For each edge, try to merge the two endpoint sets
        #
        # If union returns 1, two components became one,
        # so total components decreases by 1
        #
        # If union returns 0, they were already connected,
        # so the component count stays the same
        # --------------------------------------------------------
        for a, b in edges:
            components -= union(a, b)

        return components