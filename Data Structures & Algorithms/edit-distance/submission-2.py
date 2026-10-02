class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word2)
        # Base row: word1 is empty
        # "" -> word2[j:] needs len(word2) - j insertions
        dp = [n - j for j in range(n + 1)]
        for i in range(len(word1) - 1, -1, -1):
            new_dp = [0] * (n + 1)

            # word2 is empty -> delete remaining word1 chars
            new_dp[n] = len(word1) - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    new_dp[j] = dp[j + 1]
                else:
                    new_dp[j] = 1 + min(
                        dp[j],          # delete
                        new_dp[j + 1],  # insert
                        dp[j + 1]       # replace
                    )
            dp = new_dp
        return dp[0]  