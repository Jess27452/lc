import heapq
from typing import List


class Solution:
    def kClosest(
        self,
        points: List[List[int]],
        k: int
    ) -> List[List[int]]:

        min_heap = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            min_heap.append([distance, x, y])

        heapq.heapify(min_heap)

        result = []

        while k > 0:
            distance, x, y = heapq.heappop(min_heap)
            result.append([x, y])
            k -= 1

        return result      