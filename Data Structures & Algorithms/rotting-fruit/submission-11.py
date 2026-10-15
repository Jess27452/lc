from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0
        minutes = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Add all rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Multi-source BFS
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            minutes += 1

        if fresh > 0:
            return -1

        return minutes