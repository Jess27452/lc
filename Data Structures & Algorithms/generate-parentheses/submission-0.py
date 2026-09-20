class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            # base case: used n "(" and n ")"
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # Choice 1: add "("
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
#After stack.pop(), there is no more code inside the function.
#So Python does an automatic return,
            # Choice 2: add ")"
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res