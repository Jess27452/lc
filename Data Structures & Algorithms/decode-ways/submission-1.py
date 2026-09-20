#####
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode s[i:]
        ##3the number of ways to decode the substring starting at index i
        # Example:
        # s = "12"
        # dp[0] = number of ways to decode "12"
        # dp[1] = number of ways to decode "2"
        # dp[2] = number of ways to decode "" empty string
        #
        # Empty string has 1 way because it means we successfully decoded everything.
        dp = {len(s): 1}

        # Go from right to left
        for i in range(len(s) - 1, -1, -1):

            # If current digit is "0", it cannot be decoded alone.
            # Example:
            # "0" is invalid
            # "06" is invalid
            if s[i] == "0":
                dp[i] = 0

            else:
                # Take one digit.
                # Example:
                # if s[i] = "1", it can become "A"
                # if s[i] = "2", it can become "B"
                dp[i] = dp[i + 1]
######ways to decode "226" by taking first digit "2"
#=ways to decode the rest "26"
            # Try taking two digits.
            #
            # Valid two-digit numbers are:
            # 10, 11, 12, ..., 26
            #
            # So it is valid if:
            # s[i] == "1"
            # OR
            # s[i] == "2" and next digit is 0-6
            if (
                i + 1 < len(s)####3çDoes index i have a next character after it?
                and (
                    s[i] == "1"
                    or (s[i] == "2" and s[i + 1] in "0123456")
                )
            ):
                dp[i] += dp[i + 2]
#Then if two digits are also valid, like "22", we add:

#dp[i] += dp[i + 2]
        # dp[0] means number of ways to decode the whole string s[0:]
        return dp[0]