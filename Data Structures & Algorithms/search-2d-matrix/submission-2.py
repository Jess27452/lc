from typing import List


class Solution:
    def searchMatrix(
        self,
        matrix: List[List[int]],
        target: int
    ) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # First binary search:
        # Find the possible row.
        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = top + (bottom - top) // 2

            # Target is larger than the last value of this row.
            if target > matrix[row][-1]:
                top = row + 1

            # Target is smaller than the first value of this row.
            elif target < matrix[row][0]:
                bottom = row - 1

            # Target is within this row's value range.
            else:
                break

        # The row search failed.
        if top > bottom:
            return False

        # The selected row.
        row = top + (bottom - top) // 2

        # Second binary search:
        # Search inside the selected row.
        left = 0
        right = cols - 1

        while left <= right:
            middle = left + (right - left) // 2

            if target > matrix[row][middle]:
                left = middle + 1

            elif target < matrix[row][middle]:
                right = middle - 1

            else:
                return True

        return False