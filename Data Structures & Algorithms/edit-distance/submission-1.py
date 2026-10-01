class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = min edits to change word1[i:] -> word2[j:]
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # word1 is empty -> insert remaining word2 chars
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # word2 is empty -> delete remaining word1 chars
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Fill from bottom-right to top-left
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # Same char -> no operation
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],      # delete word1[i]
                        dp[i][j + 1],      # insert word2[j]
                        dp[i + 1][j + 1]   # replace word1[i]
                    )

        return dp[0][0]