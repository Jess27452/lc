class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def dfs(r, c, i):

            # Base case:
            # We matched every character in word
            if i == len(word):
                return True

            # Invalid cases:
            # 1. Out of bounds
            # 2. Wrong character
            # 3. Already used this cell in current path
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path
            ):
                return False

            # Choose current cell
            path.add((r, c))

            # Explore 4 directions
            res = (
                dfs(r + 1, c, i + 1) or   # down
                dfs(r - 1, c, i + 1) or   # up
                dfs(r, c + 1, i + 1) or   # right
                dfs(r, c - 1, i + 1)     # left
            )

            # Undo choice (backtracking)
            path.remove((r, c))

            return res


        # Try starting from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False