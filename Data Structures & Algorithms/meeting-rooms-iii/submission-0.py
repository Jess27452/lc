import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [room for room in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            # Release every room that is free before this meeting starts.
            while used and start >= used[0][0]:
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # If no room is free, delay this meeting.
            if not available:
                end_time, room = heapq.heappop(used)

                duration = end - start
                end = end_time + duration
#Because used is ordered by:

#(end_time, room_number)

#this gives:

#Earliest available time
#Smallest room number if times are tied
                heapq.heappush(available, room)

            # Use the smallest-numbered available room.
            room = heapq.heappop(available)

            # Mark this room as occupied until `end`.
            heapq.heappush(used, (end, room))

            count[room] += 1

        return count.index(max(count))