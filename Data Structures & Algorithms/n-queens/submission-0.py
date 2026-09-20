class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()  # r + c
        negDiag = set()  # r - c

        res = []
        board = [["."] * n for _ in range(n)]
#Go through every row
#convert each row into string
#store into list
        def backtrack(r):
            # BASE CASE
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # TRY ALL COLUMNS in current row
            for c in range(n):

                # INVALID CHOICE
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # MAKE CHOICE
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # RECURSE
                backtrack(r + 1)
                #place quenneto next row
#If a row has no valid column:

#1. recursion returns
#2. go back to previous row
#3. remove previous queen
#4. try next column in previous row
                # UNDO CHOICE
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res