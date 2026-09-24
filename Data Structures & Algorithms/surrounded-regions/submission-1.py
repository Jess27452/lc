from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        def addCell(r, c):
            # Ignore invalid cells and non-O cells
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or board[r][c] != "O"
            ):
                return

            # Mark this O as safe
            board[r][c] = "T"
            q.append((r, c))

        # Step 1: Add boundary O cells
        for r in range(ROWS):
            addCell(r, 0)
            addCell(r, COLS - 1)

        for c in range(COLS):
            addCell(0, c)
            addCell(ROWS - 1, c)

        # Step 2: BFS to mark all connected O cells
        while q:
            r, c = q.popleft()

            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)

        # Step 3: Update the board
        for r in range(ROWS):
            for c in range(COLS):

                if board[r][c] == "O":
                    board[r][c] = "X"

                elif board[r][c] == "T":
                    board[r][c] = "O"
#Boundary → Protect → Explore → Flip → Restore

#Start from boundary O cells, mark them T, and use BFS to mark all connected O cells T. Flip the remaining O cells to X, then restore T to O.