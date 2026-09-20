class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i: int, j: int) -> int:
            # We successfully matched every character in t.
            # This represents one valid subsequence.
            if j == len(t):
                return 1

            # We ran out of characters in s,
            # but t still has unmatched characters.
            if i == len(s):
                return 0#We used all characters in s, but we have not finished matching t.

            # Return a previously calculated answer.
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                # Choice 1: Use s[i] to match t[j].
                use_character = dfs(i + 1, j + 1)

                # Choice 2: Skip s[i] and continue looking
                # for another matching character in s.
                skip_character = dfs(i + 1, j)

                cache[(i, j)] = use_character + skip_character
            else:
                # s[i] cannot match t[j], so we must skip s[i].
                cache[(i, j)] = dfs(i + 1, j)

            return cache[(i, j)]

        return dfs(0, 0)