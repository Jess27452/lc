from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # invalid case
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0

            # mark current land as visited
            visit.add((r, c))

            # current cell counts as 1
            return (
                1
                + dfs(r + 1, c)   # down
                + dfs(r - 1, c)   # up
                + dfs(r, c + 1)   # right
                + dfs(r, c - 1)   # left
            )

        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
#Scan all cells

#DFS computes island size

#max(...) keeps biggest size
#if already vissted, it skips
        return area