from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        area = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            curArea = 1
            directions = [
                [1,0],
                [-1,0],
                [0,1],
                [0,-1]
            ]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit
                    ):

                        q.append((nr, nc))
                        visit.add((nr, nc))

                        curArea += 1

            return curArea

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1 and (r, c) not in visit:

                    area = max(area, bfs(r, c))

        return area