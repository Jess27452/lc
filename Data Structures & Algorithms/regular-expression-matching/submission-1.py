class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # cache[(i, j)] stores whether:
        # s[i:] matches p[j:]
        #
        # Example:
        # cache[(2, 3)] answers:
        # "Does the string starting at index 2 match
        #  the pattern starting at index 3?"
        cache = {}

        def dfs(i: int, j: int) -> bool:
            # i = current position in string s
            # j = current position in pattern p

            # If this exact state was already solved,
            # return its saved result.
            if (i, j) in cache:
                return cache[(i, j)]

            # Both the string and pattern have been completely used.
            # Therefore, the entire match was successful.
            if i >= len(s) and j >= len(p):
                return True

            # The pattern is finished, but the string may still
            # contain characters. Nothing is left in the pattern
            # to match those characters.
            if j >= len(p):
                return False

            # Check whether the current string character matches
            # the current pattern character.
            #
            # A match occurs when:
            # 1. i is still inside the string, AND
            # 2. s[i] equals p[j], OR p[j] is "."
            #
            # "." can match any single character.
            match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Check whether the NEXT pattern character is "*".
            #
            # Example:
            # p[j]     = "a"
            # p[j + 1] = "*"
            #
            # Together, "a*" means zero or more copies of "a".
            if (j + 1) < len(p) and p[j + 1] == "*":

                # There are two possible choices for "*":
                #
                # Choice 1: Use zero copies of p[j].
                # Skip both p[j] and "*".
                #
                # dfs(i, j + 2)
                #
                # Choice 2: Use at least one copy of p[j].
                # This is only possible if the current characters match.
                #
                # Move forward in the string, but stay at the same
                # pattern position because "*" may match more characters.
                #
                # match and dfs(i + 1, j)
                cache[(i, j)] = (
                    dfs(i, j + 2)
                    or
                    (match and dfs(i + 1, j))
                )

                return cache[(i, j)]

            # There is no "*" after the current pattern character.
            #
            # If the current characters match, move forward by one
            # position in both the string and pattern.
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # The current characters do not match, and there is no "*"
            # available to skip or repeat the pattern character.
            cache[(i, j)] = False
            return False

        # Begin by comparing the entire string and entire pattern:
        # s[0:] with p[0:]
        return dfs(0, 0)