from typing import List

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1

            elif c == ")":
                leftMin -= 1
                leftMax -= 1

            else:  # c == "*"
                leftMin -= 1   # if "*" becomes ")"
                leftMax += 1   # if "*" becomes "("

            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
        #leftMin = minimum possible unmatched "("
#leftMax = maximum possible unmatched "("

