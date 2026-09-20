class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []
        def backtrack(openN, closedN):

            # Base case:
            # We used n '(' and n ')'
            if openN == n and closedN == n:
                res.append("".join(stack))
                return

            # Choice 1: Add '('
            # We can only add '(' if we still have some left
            if openN < n:
                stack.append("(")

                backtrack(openN + 1, closedN)

                # Undo choice
                stack.pop()

            # Choice 2: Add ')'
            # We can only add ')' if we have unmatched '('
            if closedN < openN:
                stack.append(")")

                backtrack(openN, closedN + 1)

                # Undo choice
                stack.pop()

        backtrack(0, 0)

        return res