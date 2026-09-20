class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()   # r + c
        negDiag = set()   # r - c

        res = 0

        def backtrack(r):
            nonlocal res

            # We successfully placed queens in all n rows
            if r == n:
                res += 1
                return

            # Try putting a queen in every column of row r
            for c in range(n):

                # If this position conflicts with another queen, skip it
                if (
                    c in col
                    or (r + c) in posDiag
                    or (r - c) in negDiag
                ):
                    continue

                # Place queen at (r, c)
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                # Move to next row
                backtrack(r + 1)

                # Remove queen and try another position
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)

        return res