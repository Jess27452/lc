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
                return#STOP exploring this path immediately.

            # choose current cell
            #since we dont want repeated elements
            visit.add((r, c))

            # move in trie
            # for exmaple, if we are at root right now
            #node.chilren will be the first actual element
            node = node.children[board[r][c]]

            # build word
            word += board[r][c]

            # if current path forms a word
            ### isWord return True or False:
            if node.isWord:
                res.add(word)

            # explore 4 directions
            ##### for current node, we want to try all it neghbors
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # backtrack
            visit.remove((r, c))
           # Try a choice.
# for back tracking: Go deeper.
#If it fails or finishes,
#UNDO the choice and try another one.#

        # 2. Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)