class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):#"Who is the leader/root of x’s group?"
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x

        def union(a, b):#"Should we merge these two groups?"
            p1 = find(a)
            p2 = find(b)

            if p1 == p2:
                return False   # already connected, cycle found

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]