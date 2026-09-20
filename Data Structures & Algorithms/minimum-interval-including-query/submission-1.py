from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []#(length, right)
        res = {}

        i = 0

        for q in sorted(queries):

            # #####ADD ALL: so the one we know
            #will be the best, Add all intervals whose left <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                length = r - l + 1
                heapq.heappush(minHeap, (length, r))
                i += 1

            # Remove intervals whose right < q
            # because they do NOT contain q anymore
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # If heap not empty, smallest valid interval is on top
            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries] # it loops the 
        #loops through ORIGINAL queries:[2,3,1,7,6,8] instead of sorted one
        #and builds result list.