from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Search range includes both endpoints: [left, right]
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Find the middle index.
            middle = left + (right - left) // 2

            if nums[middle] > target:
                # Target must be to the left of middle.
                right = middle - 1

            elif nums[middle] < target:
                # Target must be to the right of middle.
                left = middle + 1

            else:
                # nums[middle] == target
                return middle

        # Target was not found.
        return -1