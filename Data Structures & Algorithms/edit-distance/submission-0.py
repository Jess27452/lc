class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # cache[i][j] means:
        # Minimum operations needed to convert word1[i:]
        # into word2[j:].
        cache = [
            [float("inf")] * (len(word2) + 1)
            for _ in range(len(word1) + 1)
        ]

        # If word1 is finished, we must insert all remaining
        # characters from word2.
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        # If word2 is finished, we must delete all remaining
        # characters from word1.
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Fill the table backward because cache[i][j] depends on:
        # cache[i + 1][j]
        # cache[i][j + 1]
        # cache[i + 1][j + 1]
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):

                # If the current characters match,
                # no operation is needed.
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]

                else:
                    # Try delete, insert, and replace.
                    cache[i][j] = 1 + min(#The 1 + means:

#Count the one edit operation you are doing right now, then add the minimum number of operations needed for the rest.
                        cache[i + 1][j],      # Delete word1[i]
                        cache[i][j + 1],      # Insert word2[j]
                        cache[i + 1][j + 1]   # Replace word1[i]
                    )

        return cache[0][0]