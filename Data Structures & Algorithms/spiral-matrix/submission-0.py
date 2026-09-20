from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        # Boundaries of the part of the matrix
        # that has not been visited yet.
        #
        # left and top are inclusive.
        # right and bottom are exclusive.
        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        # Continue while there are unvisited rows and columns.
        while left < right and top < bottom:

            # 1. Read the top row from left to right.
            for col in range(left, right):
                result.append(matrix[top][col])

            # The top row has now been visited,
            # so move the top boundary down.
            top += 1

            # 2. Read the right column from top to bottom.
            for row in range(top, bottom):
                result.append(matrix[row][right - 1])

            # The right column has now been visited,
            # so move the right boundary left.
            right -= 1

            # After shrinking top and right, check whether
            # there is still an unvisited rectangle.
            #
            # This prevents reading a row or column twice.
            if not (left < right and top < bottom):
                break

            # 3. Read the bottom row from right to left.
            for col in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][col])

            # The bottom row has now been visited,
            # so move the bottom boundary up.
            bottom -= 1

            # 4. Read the left column from bottom to top.
            for row in range(bottom - 1, top - 1, -1):
                result.append(matrix[row][left])

            # The left column has now been visited,
            # so move the left boundary right.
            left += 1

        return result