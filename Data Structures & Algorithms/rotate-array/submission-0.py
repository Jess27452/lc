from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Avoid unnecessary full rotations.
        k = k % len(nums)

        # Step 1: reverse the entire array.
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Step 2: reverse the first k elements.
        left = 0
        right = k - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Step 3: reverse everything after the first k elements.
        left = k
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1