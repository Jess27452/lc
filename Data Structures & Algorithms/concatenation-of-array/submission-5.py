from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        # Repeat the entire nums array twice.
        for i in range(2):
            # Go through every number in nums.
            for n in nums:
                # Add the current number to ans.
                ans.append(n)
        return ans