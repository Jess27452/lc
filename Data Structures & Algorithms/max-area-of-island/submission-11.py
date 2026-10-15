class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        result = 0

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r, c) in visit
                or grid[r][c] == 0
            ):
                return 0

            visit.add((r, c))

            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    result = max(result, area)

        return result