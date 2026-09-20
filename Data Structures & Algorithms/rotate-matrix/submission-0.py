from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # l = left boundary of the current layer
        # r = right boundary of the current layer
        #
        # Example for a 4 × 4 matrix:
        # First layer:  l = 0, r = 3
        # Second layer: l = 1, r = 2
        l, r = 0, len(matrix) - 1

        # Continue until the left and right boundaries meet.
        while l < r:

            # r - l is the number of groups of four elements
            # that must be rotated in the current layer.
            #
            # For a 4 × 4 outer layer:
            # r - l = 3, so i is 0, 1, 2.
            for i in range(r - l):
                top = l
                bottom = r

                # Save the top-left value because it will be overwritten.
                top_left = matrix[top][l + i]

                # Move bottom-left into top-left.
                matrix[top][l + i] = matrix[bottom - i][l]#Start at the bottom and move upward as i increases.

                # Move bottom-right into bottom-left.
                matrix[bottom - i][l] = matrix[bottom][r - i]#Start at the right boundary and move left as i increases.

                # Move top-right into bottom-right.
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move the saved top-left into top-right.
                matrix[top + i][r] = top_left#Start at the top boundary and move downward as i increases.

            # Move inward to the next layer.
            l += 1
            r -= 1