from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()

        # Insert every dictionary word into the Trie
        for word in words:
            cur = self.root

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()

                cur = cur.children[c]

            # Mark the end of a complete word
            cur.word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Trie(dictionary).root
        n = len(s)

        # dp[i] = minimum number of extra characters in s[i:]
        dp = [0] * (n + 1)

        # Calculate from right to left
        for i in range(n - 1, -1, -1):
            # Option 1: Treat s[i] as an extra character
            dp[i] = 1 + dp[i + 1]

            # Option 2: Find a dictionary word starting at i
            cur = root

            for j in range(i, n): # the first ione is alwats the same as i
                c = s[j]

                # No dictionary word has this prefix
                if c not in cur.children:
                    break

                # Move to the next Trie node
                cur = cur.children[c]

                # s[i:j+1] is a complete dictionary word
                if cur.word:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]