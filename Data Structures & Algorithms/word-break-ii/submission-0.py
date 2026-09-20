class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}

        def backtrack(i):
            # Already solved starting from index i
            if i in memo:
                return memo[i]

            # Reached the end successfully
            if i == len(s):
                return [""]

            res = []

            # Try every possible word starting at i
            for j in range(i, len(s)):
                word = s[i:j + 1]

                # Not a valid dictionary word
                if word not in wordDict:
                    continue

                # Find all sentences we can make
                # from the remaining string
                strings = backtrack(j + 1)

                for substr in strings:
                    sentence = word

                    if substr:
                        sentence += " " + substr

                    res.append(sentence)

            memo[i] = res
            return res

        return backtrack(0)