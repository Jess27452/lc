class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n - 1, -1, -1):
            total = 0
            dp[i % 4] = float("-inf")
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                dp[i % 4] = max(dp[i % 4], total - dp[(j + 1) % 4])

        if dp[0] == 0:
            return "Tie"
        return "Alice" if dp[0] > 0 else "Bob"