class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        ROWS=len(grid)
        COLS=len(grid[0])
        perim=0
        def bfs(r,c):
            nonlocal perim
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c=q.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if (nr,nc) in visit:
                        continue
                    if (
    nr not in range(ROWS)
    or nc not in range(COLS)
    or grid[nr][nc] == 0
):
                        perim+=1
                    else:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            return perim
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return bfs(i, j)
                    