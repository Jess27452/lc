class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # The bottom row has only one path from every cell:
        # keep moving right until reaching the destination.
        row = [1] * n

        # Build the remaining m - 1 rows from bottom to top.
        for _ in range(m - 1):
            new_row = [1] * n

            # Calculate from right to left.
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]

            row = new_row

        return row[0]