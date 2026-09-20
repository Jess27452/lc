from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Add one extra row and one extra column filled with zeros.
        self.sumMat = [
            [0] * (COLS + 1)
            for _ in range(ROWS + 1)
        ]

        for r in range(ROWS):
            prefix = 0

            for c in range(COLS):
                # Sum of the current row from column 0 through c.
                prefix += matrix[r][c]

                # Sum of everything above the current position.
                above = self.sumMat[r][c + 1]

                # Current prefix sum = row prefix + everything above.
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        # Convert matrix coordinates into sumMat coordinates.
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottom_right = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        top_left = self.sumMat[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left
#each cell in sumMat saves the sum of the rectangle whose bottom-right corner is that cell.

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)