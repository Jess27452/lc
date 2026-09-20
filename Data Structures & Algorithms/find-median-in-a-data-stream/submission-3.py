import heapq


class MedianFinder:

    def __init__(self):
        # Max-heap containing the smaller half.
        # Python has no built-in max-heap, so values are stored negatively.
        self.small = []

        # Min-heap containing the larger half.
        self.large = []

    def addNum(self, num: int) -> None:
        # First, add the number to the smaller-half heap.
        heapq.heappush(self.small, -num)

        # Make sure every number in small is <= every number in large.
        if (
            self.small
            and self.large
            and -self.small[0] > self.large[0]
        ):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Make sure the heaps differ in size by at most 1.
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # small contains one extra number.
        if len(self.small) > len(self.large):
            return -self.small[0]

        # large contains one extra number.
        if len(self.large) > len(self.small):
            return self.large[0]

        # Both heaps have the same size.
        return (-self.small[0] + self.large[0]) / 2