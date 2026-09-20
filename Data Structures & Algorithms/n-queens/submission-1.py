class Solution:
    def solveNQueens(self, n: int):

        col = set()
        posDiag = set()   # r + c
        negDiag = set()   # r - c

        res = []

        board = [["."] * n for _ in range(n)]

        def backtrack(r):

            # We successfully placed a queen in every row
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try putting a queen in every column of row r
            for c in range(n):

                # Is this position attacked?
                if (
                    c in col or
                    (r + c) in posDiag or
                    (r - c) in negDiag
                ):
                    continue

                # CHOOSE
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # EXPLORE next row
                backtrack(r + 1)

                # UNDO / BACKTRACK
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        return res