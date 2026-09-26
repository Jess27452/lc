class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS=len(grid[0])
        ROWS=len(grid)
        visit=set()
        island=0
        def dfs(r,c):
            if ((r,c) in visit or r not in range(ROWS) or c not in range(COLS) or grid[r][c]=="0"):
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



