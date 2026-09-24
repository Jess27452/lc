from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        # find rotten and fresh fruits
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r, c))

        def addOrange(r, c):

            nonlocal fresh

            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] != 1
            ):
                return

            # make rotten
            grid[r][c] = 2

            q.append((r, c))

            fresh -= 1

        # BFS
        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                addOrange(r + 1, c)
                addOrange(r - 1, c)
                addOrange(r, c + 1)
                addOrange(r, c - 1)

            time += 1

        return time if fresh == 0 else -1