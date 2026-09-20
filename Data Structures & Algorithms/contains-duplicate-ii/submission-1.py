from typing import List


class Solution:
    def containsNearbyDuplicate(
        self,
        nums: List[int],
        k: int
    ) -> bool:

        # Stores values from the previous at most k indexes.
        window = set()

        # Left boundary of the sliding window.
        left = 0

        for right in range(len(nums)):

            # If the index distance is greater than k,
            # remove the oldest value.
            if right - left > k:
                window.remove(nums[left])
                left += 1

            # If nums[right] is already in the window,
            # we found the same value within distance k.
            if nums[right] in window:
                return True

            # Add the current value after checking.
            window.add(nums[right])

        return False    