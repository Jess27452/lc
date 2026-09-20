from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == "+":
                # Add the previous two valid scores.
                stack.append(stack[-1] + stack[-2])

            elif op == "D":
                # Double the previous valid score.
                stack.append(2 * stack[-1])

            elif op == "C":
                # Remove the previous valid score.
                stack.pop()

            else:
                # op is a number written as a string.
                stack.append(int(op))

        return sum(stack)