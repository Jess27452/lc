class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # We must use every character from s1 and s2.
        # Therefore, their total length must equal the length of s3.
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] means:
        # Can s1[i:] and s2[j:] form s3[i + j:]?
        #
        # We use len(s1) + 1 rows and len(s2) + 1 columns
        # so we can represent the case where one or both strings
        # have been completely used.
        dp = [
            [False] * (len(s2) + 1)
            for _ in range(len(s1) + 1)
        ]

        # Base case:
        # If all characters from s1 and s2 have been used,
        # then s3 has also been completely formed.
        dp[len(s1)][len(s2)] = True

        # Fill the table from bottom-right to top-left.
        # We go backward because dp[i][j] depends on:
        # dp[i + 1][j] and dp[i][j + 1].
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):

                # Option 1: Take the next character from s1.
                #
                # i < len(s1):
                # There is still a character left in s1.
                #
                # s1[i] == s3[i + j]:
                # The current character from s1 matches the next
                # character needed in s3.
                #
                # dp[i + 1][j]:
                # After using s1[i], the remaining strings can still
                # successfully form the rest of s3.
                if (
                    i < len(s1)
                    and s1[i] == s3[i + j]
                    and dp[i + 1][j]
                ):
                    dp[i][j] = True

                # Option 2: Take the next character from s2.
                #
                # j < len(s2):
                # There is still a character left in s2.
                #
                # s2[j] == s3[i + j]:
                # The current character from s2 matches the next
                # character needed in s3.
                #
                # dp[i][j + 1]:
                # After using s2[j], the remaining strings can still
                # successfully form the rest of s3.
                if (
                    j < len(s2)
                    and s2[j] == s3[i + j]
                    and dp[i][j + 1]
                ):
                    dp[i][j] = True

        # dp[0][0] asks:
        # Can all of s1 and all of s2 form all of s3?
        return dp[0][0]