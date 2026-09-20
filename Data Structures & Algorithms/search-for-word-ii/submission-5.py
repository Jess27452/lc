from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.isWord = True


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        # Build a Trie containing all dictionary words
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0])

        result = set()
        visited = set()

        def dfs(r: int, c: int, node: TrieNode, word: str) -> None:
            # Stop when the position or Trie path is invalid
            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= cols
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            # Use the current board cell
            visited.add((r, c))

            letter = board[r][c]

            # Move to the corresponding Trie node
            node = node.children[letter]

            # Add the current letter
            word += letter

            # A complete dictionary word was found
            if node.isWord:
                result.add(word)

            # Search four directions
            dfs(r + 1, c, node, word)  # down
            dfs(r - 1, c, node, word)  # up
            dfs(r, c + 1, node, word)  # right
            dfs(r, c - 1, node, word)  # left

            # Backtrack: allow this cell to be used in another path
            visited.remove((r, c))

        # A word can start from any board position
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)