class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(len(w1)):

                # w2 ended, but w1 still has characters
                if j == len(w2):
                    return False

                # First different character
                if w1[j] != w2[j]:

                    # Wrong order
                    if orderInd[w2[j]] < orderInd[w1[j]]:
                        return False

                    # Correct order, no need to compare more letters
                    break#The first different character determines the order.

        return True