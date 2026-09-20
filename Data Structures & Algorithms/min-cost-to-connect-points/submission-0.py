from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # adj[i] stores connections from point i:
        # [cost, neighboring_point]
        adj = {i: [] for i in range(N)}

        # Calculate the cost between every pair of points.
        for i in range(N):
            x1, y1 = points[i]

            for j in range(i + 1, N):
                x2, y2 = points[j]

                distance = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([distance, j])
                adj[j].append([distance, i])

        # Prim's algorithm
        result = 0
        visited = set()

        # [connection cost, point]
        min_heap = [[0, 0]]

        while len(visited) < N:
            cost, point = heapq.heappop(min_heap)

            if point in visited:
                continue

            result += cost
            visited.add(point)

            for neighbor_cost, neighbor in adj[point]:
                if neighbor not in visited:
                    heapq.heappush(
                        min_heap,
                        [neighbor_cost, neighbor]
                    )

        return result