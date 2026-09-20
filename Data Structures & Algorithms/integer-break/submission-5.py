class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        for nums in range(2,n+1):
            dp[nums]=0 if nums==n else nums
            for i in range(1,nums):
               val=dp[i]*dp[nums-i]
               dp[nums]=max(dp[nums],val)
        return dp[n]
               