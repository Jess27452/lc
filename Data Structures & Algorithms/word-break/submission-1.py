from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means:
        # Can s[i:] be broken into words from wordDict?
        dp = [False] * (len(s) + 1)

        # Empty string is always breakable
        dp[len(s)] = True

        # Go backward from the end of s
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if word w fits starting at index i
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # If the rest after this word is breakable,
                    # then s[i:] is also breakable
                    dp[i] = dp[i + len(w)]

                # If already True, no need to check more words, it may 
                #change answer if we continue to change, but we can
                #change  dp[i] = dp[i + len(w)] to   
                #dp[i] = dp[i] or dp[i + len(w)]


                if dp[i]:
                    break

        return dp[0]