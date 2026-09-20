from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Remove duplicates and allow fast lookup.
        numSet = set(nums)

        longest = 0

        # Check each unique number.
        for n in numSet:

            # n is the beginning of a sequence only when
            # the number immediately before it does not exist.
            if n - 1 not in numSet:
                length = 0

                # Keep checking n, n + 1, n + 2, ...
                while n + length in numSet:
                    length += 1

                longest = max(longest, length)

        return longest        