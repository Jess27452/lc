class Solution:
    def isValid(self, s: str) -> bool:
        # stack will store opening brackets we haven't matched yet
        stack = []

        # map each closing bracket to the opening bracket it must match
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # go through every character in the string
        for ch in s:
            # CASE 1: ch is a closing bracket
            if ch in match:
                # if stack is empty, there is no opening bracket to match with
                if not stack:
                    return False

                # take the most recent opening bracket
                top = stack.pop()

                # check if it matches the required opening bracket
                if top != match[ch]:
                    return False

            # CASE 2: ch is an opening bracket
            else:
                stack.append(ch)

        # if stack is empty, every opening bracket got matched properly
        return len(stack) == 0