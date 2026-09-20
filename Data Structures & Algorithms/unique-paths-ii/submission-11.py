class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M,N=len(grid),len(grid[0])
        dp=[0]*N
        dp[-1]=1
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if grid[i][j]==1:
                    dp[j]=0
                elif j+1<N:
                    dp[j]=dp[j]+dp[j+1]
        return dp[0]
                
