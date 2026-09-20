class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        self.rank[px] += self.rank[py]

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Add original index to every edge
        for i in range(len(edges)):
            edges[i].append(i)

        # Sort by weight
        edges.sort(key=lambda e: e[2])

        # ------------------------------------------------
        # Step 1: Find normal MST weight
        # ------------------------------------------------
        uf = UnionFind(n)
        mst_weight = 0

        for n1, n2, weight, index in edges:
            if uf.union(n1, n2):
                mst_weight += weight

        critical = []
        pseudo = []

        # ------------------------------------------------
        # Step 2: Test every edge
        # ------------------------------------------------
        for n1, n2, e_weight, i in edges:

            # --------------------------------------------
            # Test 1: Build MST WITHOUT current edge
            # --------------------------------------------
            uf = UnionFind(n)
            weight = 0

            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w

            # If graph is disconnected
            # OR MST becomes more expensive
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            # --------------------------------------------
            # Test 2: Build MST WITH current edge forced
            # --------------------------------------------
            uf = UnionFind(n)

            # Force current edge first
            uf.union(n1, n2)
            weight = e_weight

            # Finish the MST normally
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w

            # If we can still get the normal MST weight,
            # this edge can be part of some MST
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]