from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Special case:
        # If there is only one house, just rob it.
        if len(nums) == 1:
            return nums[0]

        # Because houses are in a circle:
        # we cannot rob both nums[0] and nums[-1].
        #
        # So we try two choices:
        #
        # 1. Exclude the first house:
        #    nums[1:]
        #
        # 2. Exclude the last house:
        #    nums[:-1]
        #
        # Then choose the bigger result.
        return max(
            self.helper(nums[1:]),   # rob houses from index 1 to end
            self.helper(nums[:-1])   # rob houses from index 0 to second-last
        )

    def helper(self, nums: List[int]) -> int:
        # This is the same logic as House Robber I.
        #
        # rob1 = best money from two houses before
        # rob2 = best money from previous house
        rob1, rob2 = 0, 0

        for n in nums:
            # Choice 1:
            # Rob current house n.
            # Then we can only add rob1, because rob1 is two houses before.
            #
            # Choice 2:
            # Skip current house.
            # Then keep rob2.
            newRob = max(rob1 + n, rob2)

            # Move forward.
            # Old rob2 becomes rob1.
            rob1 = rob2

            # Current best becomes rob2.
            rob2 = newRob

        # After checking all houses, rob2 is the answer.
        return rob2