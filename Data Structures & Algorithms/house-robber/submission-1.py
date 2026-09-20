from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 = max money we can rob up to two houses before
        # rob2 = max money we can rob up to the previous house
        rob1, rob2 = 0, 0

        # Go through each house's money
        for n in nums:
            # If we rob current house:
            # we get n + rob1
            # because rob1 is from two houses before, so it is safe.
            #
            # If we skip current house:
            # we keep rob2
            # because rob2 is the best answer up to the previous house.
            #
            # Choose the bigger one.
            temp = max(n + rob1, rob2)

            # Move forward:
            # old rob2 becomes rob1
            rob1 = rob2

            # current best becomes rob2
            rob2 = temp

        # rob2 stores the maximum money after checking all houses
        return rob2