class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # Odd total can never be split into two equal sums
        if total % 2:
            return False
        target = total // 2
        # dp[s] = whether we can make sum s
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            # Go backwards so each number is only used once
            for s in range(target, n - 1, -1):
                dp[s] = dp[s] or dp[s - n]
        return dp[target]