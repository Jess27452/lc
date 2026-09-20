from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1:
        # Find a position inside the cycle.
        slow = 0
        fast = 0

        while True:
            # Move slow one step.
            slow = nums[slow]

            # Move fast two steps.
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2:
        # Find the entrance of the cycle.
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow