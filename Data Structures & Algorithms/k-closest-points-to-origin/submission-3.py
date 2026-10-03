import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y

            # Negative distance makes this act like a max heap
            heapq.heappush(heap, (-dist, x, y))

            # Only keep k closest points
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for dist, x, y in heap]