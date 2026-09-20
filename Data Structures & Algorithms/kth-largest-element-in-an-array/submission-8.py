import heapq


class Solution:
    def findKthLargest(self, nums, k):
        min_heap = []

        for num in nums:
            # Add the current number
            heapq.heappush(min_heap, num)

            # Keep only the k largest numbers
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The smallest among the k largest numbers
        return min_heap[0]