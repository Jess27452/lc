class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        # Store the LAST index where each character appears
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []

        size = 0
        end = 0

        for i, c in enumerate(s):
            # Current partition gets one character bigger
            size += 1

            # The partition must extend at least to
            # the last occurrence of this character
            end = max(end, lastIndex[c])

            # If we reached the required end,
            # this partition is complete
            if i == end:
                res.append(size)
                size = 0

        return res