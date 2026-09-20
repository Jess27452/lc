from typing import List
import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add each task's original index.
        # [enqueueTime, processingTime]
        # becomes:
        # [enqueueTime, processingTime, originalIndex]
        for index, task in enumerate(tasks):
            task.append(index)

        # Sort tasks by enqueue time.
        tasks.sort(key=lambda task: task[0])

        result = []

        # Stores:
        # (processingTime, originalIndex)
        min_heap = []

        # Points to the next task that has not been added to the heap.
        i = 0

        # The current CPU time.
        time = 0

        while min_heap or i < len(tasks):

            # Add every task that has already arrived.
            while i < len(tasks) and tasks[i][0] <= time:
                enqueue_time, processing_time, original_index = tasks[i]

                heapq.heappush(
                    min_heap,
                    (processing_time, original_index)
                )

                i += 1

            # If no task is currently available, jump forward to the
            # enqueue time of the next task.
            if not min_heap:
                time = tasks[i][0]
                continue

            # Select the task with:
            # 1. The shortest processing time
            # 2. The smallest original index when tied
            processing_time, original_index = heapq.heappop(min_heap)

            # Run this task completely.
            time += processing_time

            # Record which task was processed.
            result.append(original_index)

        return result