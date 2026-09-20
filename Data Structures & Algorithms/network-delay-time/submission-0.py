from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        # Store each node's outgoing connections.
        # edges[u] contains (destination, travel_time).
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        # Each heap item is:
        # (total_time_from_k, node)
        minHeap = [(0, k)]

        # Stores nodes whose shortest arrival time is finalized.
        visit = set()

        # Time needed to reach the latest visited node.
        t = 0

        while minHeap:
            # Remove the reachable node with the smallest total time.
            w1, n1 = heapq.heappop(minHeap)

            # Ignore it if we already processed this node.
            if n1 in visit:
                continue

            visit.add(n1)

            # Update the latest signal arrival time.
            t = max(t, w1)

            # Check every node reachable from n1.
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # Total time to n2 =
                    # time to n1 + time from n1 to n2
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # Return t if every node received the signal.
        # Otherwise, return -1.
        return t if len(visit) == n else -1