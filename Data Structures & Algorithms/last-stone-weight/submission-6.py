from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert Python's min-heap into a max-heap
        # by making every weight negative.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # The two smallest negative numbers represent
            # the two largest original stones.
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # Different weights: push the remaining stone back.
            if second > first:
                heapq.heappush(stones, first - second)

        # Protect against an empty heap.
        stones.append(0)

        return abs(stones[0])