class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)
        dp = [[0] * n for _ in range(n)]
        # length = distance between left and right
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = (
                        dp[left][k]
                        + balloons[left] * balloons[k] * balloons[right]
                        + dp[k][right]
                    )
                    dp[left][right] = max(
                        dp[left][right],
                        coins
                    )
        return dp[0][n - 1]