class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        # i = 0 -> choose letter for first digit
        #i = 1 -> choose letter for second digit
        def backtrack(i, curStr):

            # BASE CASE
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # TRY ALL CHOICES for current digit
            for c in digitToChar[digits[i]]:

                # MAKE CHOICE + RECURSE
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res