from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        # Convert nums into a min-heap
        heapq.heapify(self.minHeap)

        # Keep only the k largest numbers
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new number
        heapq.heappush(self.minHeap, val)

        # If there are more than k numbers,
        # remove the smallest one
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # Smallest among the k largest numbers
        return self.minHeap[0]