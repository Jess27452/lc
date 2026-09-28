from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        INF=2147483647
        # 1. Put ALL treasure cells into queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 2. Multi-source BFS
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newr = r + dr
                    newc = c + dc

                    if (
                        newr in range(ROWS)
                        and newc in range(COLS)
                        and (newr, newc) not in visit
                        and grid[newr][newc] ==INF
                    ):
                        visit.add((newr, newc))
                        q.append((newr, newc))
                        grid[newr][newc] = dist


            dist += 1
