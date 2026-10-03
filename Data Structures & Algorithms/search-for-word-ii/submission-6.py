from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build Trie
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            # out of bounds or already used
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "#"
            ):
                return

            ch = board[r][c]

            # no dictionary word has this prefix
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # found a complete word
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None   # avoid duplicates

            # mark visited
            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # backtrack
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res