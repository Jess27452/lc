from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]

        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque()

            for r, c in source:
                if not ocean[r][c]:
                    ocean[r][c] = True
                    q.append((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and not ocean[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        ocean[nr][nc] = True
                        q.append((nr, nc))

        # Step 1: Find ocean boundary cells
        pacific = []
        atlantic = []

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        # Step 2: BFS from both oceans
        bfs(pacific, pac)
        bfs(atlantic, atl)

        # Step 3: Find cells reachable by both oceans
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res