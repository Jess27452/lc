from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Search interval is [left, right].
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                # Target belongs to the right of middle.
                left = middle + 1

            else:
                # Target belongs to the left of middle.
                right = middle - 1

        # When the loop ends, left is the correct insertion index.
        return left