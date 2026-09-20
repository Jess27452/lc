from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # The first row is also being used to store column markers.
        # Therefore, we need a separate variable to remember whether
        # the original first row itself should become all zeroes.
        rowZero = False

        # First pass:
        # Find every original zero and create markers.
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:

                    # Mark this column for zeroing.
                    # We store the marker in the first row.
                    matrix[0][c] = 0

                    if r > 0:
                        # Mark this row for zeroing.
                        # We store the marker in the first column.
                        matrix[r][0] = 0
                    else:
                        # The zero is already in the first row.
                        # We cannot use matrix[0][0] alone to remember
                        # both the first row and first column.
                        rowZero = True

        # Second pass:
        # Zero the inside of the matrix using the markers.
        #
        # Start at row 1 and column 1 because the first row
        # and first column currently contain our markers.
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # matrix[r][0] == 0 means row r should become zero.
                # matrix[0][c] == 0 means column c should become zero.
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # If matrix[0][0] is zero, the first column
        # needs to become all zeroes.
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # If rowZero is True, the first row
        # needs to become all zeroes.
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

                #First pass:
#Find original zeroes and create markers.

#Second pass:
#Use markers to zero the inside cells.

#Final steps:
#Use matrix[0][0] to handle the first column.
#Use rowZero to handle the first row.