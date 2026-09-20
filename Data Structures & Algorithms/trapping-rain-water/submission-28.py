from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # If the array is empty, no water can be trapped.
        if not height:
            return 0

        # left starts at the first bar.
        left = 0

        # right starts at the last bar.
        right = len(height) - 1

        # Tallest bar seen so far from the left side.
        left_max = height[left]

        # Tallest bar seen so far from the right side.
        right_max = height[right]

        # Total amount of trapped water.
        water = 0

        # Continue until the two pointers meet.
        while left < right:

            # The smaller maximum controls the water level.
            if left_max < right_max:
                # Move the left pointer inward.
                left += 1

                # Update the tallest bar seen from the left.
                left_max = max(left_max, height[left])

                # Water at this position:
                #
                # left_max        = maximum possible water height
                # height[left]    = height of the current bar
                #
                # Example:
                # left_max = 4
                # current bar = 2
                # trapped water = 4 - 2 = 2
                water += left_max - height[left]

            else:
                # Move the right pointer inward.
                right -= 1

                # Update the tallest bar seen from the right.
                right_max = max(right_max, height[right])

                # Calculate water trapped at this position.
                water += right_max - height[right]

        # Return the total amount of trapped water.
        return water