class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rs=len(grid)
        cs=len(grid[0])
        visit=set()
        island=0
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))# the visst here only includes the grids that are 1
            q.append([r,c])
            while q:# this bfs ends when q is empty
                row,col=q.popleft()
                directions=[[0,-1],[0,1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r=dr+row
                    c=dc+col
                    if ((r,c) not in visit and r in range(rs) and c in range(cs) and grid[r][c]=="1"):
                            visit.add((r,c))
                            q.append([r,c])
        for r in range(rs):
            for c in range(cs):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island
                        

            