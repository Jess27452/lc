import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        adj = defaultdict(list)

        # Build graph
        for u, v, t in times:
            adj[u].append((v, t))

        # (time from k, node)
        minHeap = [(0, k)]

        # node -> shortest time from k
        dist = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)

            # Already found shortest path to this node
            if node in dist:
                continue

            # First time popped = shortest distance
            dist[node] = time

            # Explore neighbors
            for nei, weight in adj[node]:
                    heapq.heappush(
                        minHeap,
                        (time + weight, nei)
                    )

        # Some node cannot be reached
        if len(dist) != n:
            return -1

        # Last node to receive signal
        return max(dist.values())