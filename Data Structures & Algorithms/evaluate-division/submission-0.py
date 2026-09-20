from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        adj = defaultdict(list)

        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0

            q = deque([(src, 1.0)])
            visit = {src}

            while q:
                node, weight = q.popleft()

                if node == target:
                    return weight

                for nei, edge_weight in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, weight * edge_weight))

            return -1.0

        res = []

        for src, target in queries:
            res.append(bfs(src, target))

        return res