from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # ------------------------------------------------------
        # ROWS and COLS store the size of the board.
        #
        # Example:
        # board = [
        #   ["A","B","C","D"],
        #   ["S","A","A","T"],
        #   ["A","C","A","E"]
        # ]
        #
        # Then:
        # ROWS = 3
        # COLS = 4
        # ------------------------------------------------------
        ROWS, COLS = len(board), len(board[0])

        # ------------------------------------------------------
        # path = set of cells currently used in the current DFS path
        #
        # IMPORTANT:
        # path is NOT used to match the letters.
        #
        # Letter matching is done by:
        #     board[r][c] == word[i]
        #
        # path is used to enforce the rule:
        # "The same cell may not be used more than once."
        #
        # Example:
        # if path = {(0,2), (1,2)}
        # that means in the CURRENT recursive path,
        # those cells are already used,
        # so we cannot step on them again.
        # ------------------------------------------------------
        path = set()

        def dfs(r: int, c: int, i: int) -> bool:
            """
            DFS tries to answer this question:

            Can we match word[i:] starting from board cell (r, c)?

            Parameters:
            r = current row
            c = current column
            i = current index in the word

            Example:
            if word = "CAT"
            then:
                dfs(0, 2, 0) means:
                "Can I match 'CAT' starting at board[0][2]?"

                dfs(1, 2, 1) means:
                "Can I match 'AT' starting at board[1][2]?"
            """

            # --------------------------------------------------
            # BASE CASE 1:
            # If i == len(word), that means we already matched
            # every character in the word successfully.
            #
            # Example:
            # word = "CAT"
            # len(word) = 3
            #
            # if i becomes 3, that means:
            # - C matched
            # - A matched
            # - T matched
            # so we return True
            # --------------------------------------------------
            if i == len(word):
                return True

            # --------------------------------------------------
            # BASE CASE 2:
            # Return False if any invalid condition happens:
            #
            # 1. out of bounds
            # 2. current board letter does not match word[i]
            # 3. current cell is already used in the current path
            #
            # VERY IMPORTANT:
            #
            # board[r][c] != word[i]
            #     checks LETTER MATCH
            #
            # (r, c) in path
            #     checks CELL REUSE
            #
            # These are two completely different checks.
            #
            # Example:
            # board = [["A","B"]]
            # word = "ABA"
            #
            # We could try:
            # A at (0,0)
            # B at (0,1)
            # A at (0,0) again
            #
            # The letter matches, BUT reusing (0,0) is illegal.
            # That is why path is needed.
            # --------------------------------------------------
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path
            ):
                return False

            # --------------------------------------------------
            # Mark current cell as used in this current path.
            #
            # Example:
            # if we match 'C' at (0,2),
            # then path becomes {(0,2)}
            #
            # if next we match 'A' at (1,2),
            # then path becomes {(0,2), (1,2)}
            #
            # This means:
            # do not reuse these cells while exploring this branch
            # --------------------------------------------------
            path.add((r, c))

            # --------------------------------------------------
            # Explore the 4 directions for the next character:
            # down, up, right, left
            #
            # We increment i to i+1 because we already matched
            # word[i] at the current cell.
            #
            # If ANY one of these recursive calls returns True,
            # then the whole result is True.
            #
            # Python's "or" short-circuits:
            # if the first call returns True,
            # Python stops and does not check the rest.
            # --------------------------------------------------
            res = (
                dfs(r + 1, c, i + 1) or   # down
                dfs(r - 1, c, i + 1) or   # up
                dfs(r, c + 1, i + 1) or   # right
                dfs(r, c - 1, i + 1)      # left
            )

            # --------------------------------------------------
            # BACKTRACKING HAPPENS HERE
            #
            # We remove the current cell from path before returning.
            #
            # Why?
            # Because path should only contain cells used in the
            # CURRENT recursive branch.
            #
            # If we do NOT remove it, then the cell stays blocked
            # forever, even for other branches where it should be
            # allowed again.
            #
            # Example:
            # Suppose one branch used (1,2) and failed.
            # Then we want to try another branch.
            # If we never remove (1,2), future branches incorrectly
            # think (1,2) is still in use.
            #
            # So:
            # path.add((r, c))   -> choose / mark visited
            # explore neighbors
            # path.remove((r, c)) -> undo choice / backtrack
            # --------------------------------------------------
            path.remove((r, c))

            # Return whether any neighbor path worked
            return res

        # ------------------------------------------------------
        # Try every cell as a starting point.
        #
        # Why?
        # Because the first letter of the word could begin anywhere
        # on the board.
        #
        # Example:
        # if word starts with 'C',
        # we do not know which 'C' on the board is the correct start,
        # so we test all cells.
        # ------------------------------------------------------
        for r in range(ROWS):
            for c in range(COLS):
                # Start searching the whole word from cell (r, c)
                if dfs(r, c, 0):
                    return True

        # If no starting position works, the word does not exist
        return False