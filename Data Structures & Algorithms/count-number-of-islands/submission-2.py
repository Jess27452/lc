from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):

            # invalid case
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == "0" or
                (r, c) in visit
            ):
                return

            # mark visited
            visit.add((r, c))

            # explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):

                # found new island
                if grid[r][c] == "1" and (r, c) not in visit:

                    dfs(r, c)
                    islands += 1

        return islands