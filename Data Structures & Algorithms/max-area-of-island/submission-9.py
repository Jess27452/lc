class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxarea = 0

        def dfs(r, c):
            if (
                r in range(rows)
                and c in range(cols)
                and grid[r][c] == 1
                and (r, c) not in visit
            ):
                visit.add((r, c))

                area = 1
                area += dfs(r + 1, c)
                area += dfs(r - 1, c)
                area += dfs(r, c + 1)
                area += dfs(r, c - 1)

                return area

            return 0#return 0 if invalid

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxarea = max(maxarea, dfs(r, c))

        return maxarea