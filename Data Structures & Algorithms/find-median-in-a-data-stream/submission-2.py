import heapq

class MedianFinder:
#timecompelxity for lookup is o(1) but for push/pop is o(logn)
    def __init__(self):
        # small = max heap for smaller half
        # Python only has min heap, so store negative numbers
        self.small = []
        # large = min heap for larger half
        self.large = []
    def addNum(self, num: int) -> None:
        # 1. Always add to small first
        heapq.heappush(self.small, -num)
        # 2. Fix order:
        # largest in small should be <= smallest in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 3. Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    def findMedian(self) -> float:
        # odd number of total elements
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        # even number of total elements
        return (-self.small[0] + self.large[0]) / 2.0