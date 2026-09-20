from collections import Counter, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Python has a min-heap, so use negative counts
        # to simulate a max-heap.
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
#max_heap = tasks available now
#queue    = tasks waiting for cooldown
        time = 0

        # Each item is:
        # [remaining negative count, cooldown finishing time]
        queue = deque()

        while max_heap or queue:
            time += 1

            # Execute the currently most frequent available task.
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                # If this task still has copies left,
                # place it into cooldown.
                if cnt:
                    queue.append([cnt, time + n])

            # Put a task back into the heap when its cooldown ends.
            if queue and queue[0][1] == time:
                cnt, ready_time = queue.popleft()
                heapq.heappush(max_heap, cnt)

        return time