class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        row=N*[0]
        row[-1]=1
        for i in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[i][c]==1:
                    row[c]=0
                elif c+1<N:
                    row[c]=row[c+1]+row[c]
        return row[0]