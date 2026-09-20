import heapq

class MedianFinder:

    def __init__(self):
        """
        self.small = max heap for the smaller half
                     but implemented using negative numbers
        self.large = min heap for the larger half
        """
        self.small = []   # stores negatives, so acts like a max heap
        self.large = []   # normal min heap

    def addNum(self, num: int) -> None:
        """
        Add a number into the data structure.
        """

        # ---------------------------------------------------
        # STEP 1: Always push into self.small first
        # Since self.small is a max heap simulated by negatives,
        # we store -num instead of num
        # ---------------------------------------------------
        heapq.heappush(self.small, -num)

        # ---------------------------------------------------
        # STEP 2: Make sure ordering is correct
        #
        # Rule we want:
        # every value in small <= every value in large
        #
        # The largest value in small is -self.small[0]
        # The smallest value in large is self.large[0]
        #
        # If largest(small) > smallest(large),
        # move that value from small to large
        # ---------------------------------------------------
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)   # convert back to positive
            heapq.heappush(self.large, val)

        # ---------------------------------------------------
        # STEP 3: Rebalance sizes if one heap is too big
        #
        # We only allow size difference at most 1
        # ---------------------------------------------------

        # If small has 2 more than large, move one to large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # If large has 2 more than small, move one to small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        """
        Return the median of all added numbers.
        """

        # ---------------------------------------------------
        # If small has more elements,
        # median is the top of small
        # but convert negative back to positive
        # ---------------------------------------------------
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # ---------------------------------------------------
        # If large has more elements,
        # median is the top of large
        # ---------------------------------------------------
        if len(self.large) > len(self.small):
            return float(self.large[0])

        # ---------------------------------------------------
        # If same size,
        # median is average of:
        # largest value in small and smallest value in large
        # ---------------------------------------------------
        return (-self.small[0] + self.large[0]) / 2.0