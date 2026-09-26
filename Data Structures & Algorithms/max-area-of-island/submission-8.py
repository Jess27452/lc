class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        maxarea=0
        def dfs(r,c):
            area=0
            if (
                r >= len(grid)
                or c >= len(grid[0])
                or r < 0
                or c < 0
                or grid[r][c] == 0
            ) or (r,c) in visit:
                return 0
            else:
                visit.add((r,c))
                area=dfs(r+1,c)+area+1
                area=dfs(r,c+1)+area
                area=dfs(r,c-1)+area
                area=dfs(r-1,c)+area
            return area
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j]==1:
                    area=dfs(i,j)
                    maxarea=max(area,maxarea)
        return maxarea