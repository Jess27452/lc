from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # If nums contains n numbers, the complete range is:
        # 0, 1, 2, ..., n
        #
        # The loop below includes indices 0 through n - 1,
        # so we start res with n to include the final expected number.
        res = len(nums)

        # i represents a number that SHOULD appear in the range.
        # nums[i] represents a number that ACTUALLY appears.
        for i in range(len(nums)):
            # Add an expected number i,
            # then subtract an actual number nums[i].
            res += i - nums[i]

        # Everything appearing in both groups cancels out.
        # The only value remaining is the missing number.
        return res