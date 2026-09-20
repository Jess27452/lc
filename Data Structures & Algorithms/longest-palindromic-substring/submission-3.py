class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        maxLen = 1

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLen = 2

        # length >= 3
        for length in range(3, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = True

                    if length > maxLen:
                        start = left
                        maxLen = length

        return s[start:start + maxLen]