from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (start_index, height)

        for i, h in enumerate(heights + [0]):  # add sentinel 0 to flush stack
            start = i

            # If current bar is lower, close out rectangles of taller bars
            while stack and h < stack[-1][1]:
                start_prev, height_prev = stack.pop()
                max_area = max(max_area, height_prev * (i - start_prev))
                start = start_prev  # new bar can extend further left

            stack.append((start, h))

        return max_area