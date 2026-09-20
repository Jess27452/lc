class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0

        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])

            i += 1
            j += 1

        # Add any characters remaining in word1.
        result.append(word1[i:])
# if it reaches to the end result.append("")

#There is nothing left in word1, so it appends an empty string.
        # Add any characters remaining in word2.
        result.append(word2[j:])

        return "".join(result)