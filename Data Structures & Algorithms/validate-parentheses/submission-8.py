class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # c is a closing bracket
            if c in close_to_open:
                # The most recent opening bracket must match c.
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False

            # c is an opening bracket
            else:
                stack.append(c)

        # Valid only if no unmatched opening brackets remain.
        return not stack