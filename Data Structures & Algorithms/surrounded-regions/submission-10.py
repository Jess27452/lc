from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()

        # 1. Find border O's and mark them safe as T
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "T"
                q.append((r, 0))

            if board[r][COLS - 1] == "O":
                board[r][COLS - 1] = "T"
                q.append((r, COLS - 1))

        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "T"
                q.append((0, c))

            if board[ROWS - 1][c] == "O":
                board[ROWS - 1][c] = "T"
                q.append((ROWS - 1, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 2. BFS from safe border O's
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
#We start from every "O" on the border and expand to neighboring "O" cells using BFS.
                if (
                    nr in range(ROWS)
                    and nc in range(COLS)
                    and board[nr][nc] == "O"
                ):
                    board[nr][nc] = "T"
                    q.append((nr, nc))

        # 3. Reverse
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"