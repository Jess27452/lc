from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 1. Put all words into Trie
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            # invalid cases
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            # choose current cell
            visit.add((r, c))

            # move in trie
            node = node.children[board[r][c]]

            # build word
            word += board[r][c]

            # if current path forms a word
            if node.isWord:
                res.add(word)

            # explore 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # backtrack
            visit.remove((r, c))

        # 2. Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)