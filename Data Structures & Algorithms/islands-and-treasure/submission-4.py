from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and (nr, nc) not in visit
                        and grid[nr][nc] == 2147483647
                    ):
                        grid[nr][nc] = dist + 1
                        q.append((nr, nc))
                        visit.add((nr, nc))

            dist += 1
