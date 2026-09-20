class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:  # "/"
                    stack.append(int(a / b))  # trunc toward 0
            else:
                stack.append(int(t))

        return stack[-1]