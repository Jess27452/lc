
       # time compleixty o(n*m) m is idel time and n is the task


       #X re-enters heap during cycle 3
       # whe n=2
       #x goes into when tme is 1
 #Current code treats:

#cooldown completion

#as happening at END of cycle.

#So task usable starting NEXT cycle.
from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears
        # Example: ["A","A","A","B","C"]
        # count = {"A": 3, "B": 1, "C": 1}
        count = Counter(tasks)

        # Python heapq is a MIN heap.
        # We use negative counts to simulate a MAX heap.
        # Example counts [3,1,1] -> heap [-3,-1,-1]
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Queue stores tasks that are cooling down
        # Each item is [remaining_count, available_time]
        q = deque()

        # CPU cycle counter
        time = 0

        # Continue while there are available tasks OR cooling tasks
        while maxHeap or q:
            time += 1

            # If there is an available task, run the most frequent one
            if maxHeap:
                cnt = heapq.heappop(maxHeap)

                # We used this task once
                # Since cnt is negative, adding 1 reduces remaining count
                cnt += 1

                # If task still has remaining count, put it into cooldown
                if cnt != 0:
                    q.append([cnt, time + n])

            # If the first cooling task is ready, move it back to heap
            if q and q[0][1] == time:
                ready_task = q.popleft()
                heapq.heappush(maxHeap, ready_task[0])

        return time