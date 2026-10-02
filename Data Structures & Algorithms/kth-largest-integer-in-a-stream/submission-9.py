import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # If we have more than k elements,
        # remove the smallest one
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Smallest among the k largest = kth largest
        return self.heap[0]