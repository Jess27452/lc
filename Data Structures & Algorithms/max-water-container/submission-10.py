from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0

        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left

            container_height = min(
                height[left],
                height[right]
            )

            area = width * container_height

            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result