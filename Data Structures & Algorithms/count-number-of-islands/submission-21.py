class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        COLS = len(grid[0])
        ROWS = len(grid)
        visit = set()
        island = 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c):
            if (
                (r, c) in visit
                or r not in range(ROWS)
                or c not in range(COLS)
                or grid[r][c] == "0"
            ):
                return

            visit.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    island += 1

        return island


