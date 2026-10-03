import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        # Sort by meeting start time
        intervals.sort(key=lambda x: x.start)

        minHeap = []

        for interval in intervals:
            # Earliest room is free
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)

            # Current meeting occupies a room until interval.end
            heapq.heappush(minHeap, interval.end)

        return len(minHeap)