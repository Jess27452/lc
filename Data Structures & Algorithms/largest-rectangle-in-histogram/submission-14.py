from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []   # each item: (starting_index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                width = i - index
                maxArea = max(maxArea, height * width)

                start = index
    #A shorter bar stops taller rectangles, but it can inherit their left boundary because the previous taller bars are also tall enough to support the shorter rectangle.
            stack.append((start, h))

        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, h * width)

        return maxArea
    # Time:  O(n)
    #Space: O(n)