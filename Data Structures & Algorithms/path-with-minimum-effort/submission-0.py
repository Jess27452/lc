class Solution:
    def minimumEffortPath(self, heights):

        ROWS, COLS = len(heights), len(heights[0])

        minHeap = [[0, 0, 0]]   # [effort, row, col]

        visit = set()

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        while minHeap:

            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:

                newR = r + dr
                newC = c + dc

                if (
                    newR < 0 or
                    newC < 0 or
                    newR == ROWS or
                    newC == COLS or
                    (newR, newC) in visit
                ):
                    continue

                newDiff = max(
                    diff,
                    abs(
                        heights[r][c] -
                        heights[newR][newC]
                    )
                )

                heapq.heappush(
                    minHeap,
                    [newDiff, newR, newC]
                )