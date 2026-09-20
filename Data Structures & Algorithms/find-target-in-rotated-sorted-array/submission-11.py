from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            # Target found.
            if target == nums[middle]:
                return middle

            # Case 1: The left half is sorted.
            if nums[left] <= nums[middle]:

                # Target is NOT inside the sorted left half.
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1

            # Case 2: The right half is sorted.
            else:

                # Target is NOT inside the sorted right half.
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1