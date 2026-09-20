from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # dp[(r, c)] stores the length of the longest increasing
        # path starting from cell (r, c).
        dp = {}

        def dfs(r: int, c: int, previous_value: int) -> int:
            # Stop if:
            # 1. We leave the matrix.
            # 2. The current value is not greater than the previous value.
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or matrix[r][c] <= previous_value
            ):
                return 0

            # If this cell was already solved, return its saved answer.
            if (r, c) in dp:
                return dp[(r, c)]

            # The path contains at least the current cell.
            result = 1

            # Try moving down.
            result = max(
                result,
                1 + dfs(r + 1, c, matrix[r][c])
            )

            # Try moving up.
            result = max(result,1 + dfs(r - 1, c, matrix[r][c]))

            # Try moving right.
            result = max(
                result,
                1 + dfs(r, c + 1, matrix[r][c])
            )

            # Try moving left.
            result = max(
                result,
                1 + dfs(r, c - 1, matrix[r][c])
            )

            # Save the answer for this cell.
            dp[(r, c)] = result
            return result

        # We need to try starting from every cell.
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, float("-inf"))

        # The answer is the longest path starting from any cell.
        return max(dp.values())