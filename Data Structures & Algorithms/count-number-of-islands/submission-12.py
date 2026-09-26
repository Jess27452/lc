class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS=len(grid)
        COLS=len(grid[0])
        visit=set()
        island=0
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or grid[r][c]=="0":
                return
            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        return island
