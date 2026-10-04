class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Make text2 the shorter string to save space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        # Go backwards through text1
        for i in range(len(text1) - 1, -1, -1):
            newDp = [0] * (len(text2) + 1)

            # Go backwards through text2
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    # Matching chars: use both chars
                    newDp[j] = 1 + dp[j + 1]
                else:
                    # Skip one char from either string
                    newDp[j] = max(dp[j], newDp[j + 1])

            dp = newDp

        return dp[0]