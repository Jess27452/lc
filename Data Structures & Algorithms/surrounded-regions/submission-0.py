from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            # invalid case
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                board[r][c] != "O"
            ):
                return

            # mark safe O as temporary T
            board[r][c] = "T"

            # explore 4 directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: mark border-connected O as T
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    board[r][c] == "O"
                    and (r in [0, ROWS - 1] or c in [0, COLS - 1])
                ):#only includes two numbers [0,ROWs-1]
                    capture(r, c)

        # Step 2: flip surrounded O to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Step 3: turn safe T back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"