class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS=len(grid)
        COLS=len(grid[0])
        visit=set()
        islands=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col=q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nrow=row+dr
                    ncol=col+dc
                    if (
                        nrow in range(ROWS)
                        and ncol in range(COLS)
                        and grid[nrow][ncol] == "1"
                        and (nrow,ncol) not in visit
                    ):
                        q.append((nrow,ncol))
                        visit.add((nrow,ncol))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands


