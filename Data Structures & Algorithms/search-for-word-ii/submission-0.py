from typing import List


class TrieNode:
    def __init__(self):
        # maps character -> next TrieNode
        self.children = {}

        # True if a full word ends at this node
        self.isWord = False

    def addWord(self, word):
        # start at this node (usually the trie root)
        cur = self

        # insert the word one character at a time
        for c in word:
            # if this character path does not exist yet, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # move to the next trie node for this character
            cur = cur.children[c]

        # after the last character, mark this node as a full word
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # -----------------------------------
        # 1. Build a trie from all the words
        # -----------------------------------
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # board dimensions
        ROWS, COLS = len(board), len(board[0])

        # res stores found words
        # use a set so duplicates are automatically removed
        res = set()

        # visit stores board cells currently used in the DFS path
        # this prevents using the same cell twice in one word
        visit = set()

        # dfs(r, c, node, word) means:
        # - we are currently at board cell (r, c)
        # - we are currently at trie node "node"
        # - "word" is the string built so far from the board path
        def dfs(r, c, node, word):
            # -----------------------------------
            # 2. Stop if this path is invalid
            # -----------------------------------

            # stop if row/col is outside the board
            # stop if this board letter is not a valid next trie child
            # stop if this cell is already used in current path
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] not in node.children or
                (r, c) in visit
            ):
                return

            # -----------------------------------
            # 3. Use the current board cell
            # -----------------------------------

            # mark this cell as used in the current path
            visit.add((r, c))

            # move to the trie child for the current board letter
            node = node.children[board[r][c]]

            # add this board letter to the current built word
            word += board[r][c]

            # -----------------------------------
            # 4. If this trie node ends a word,
            #    then we found a valid word
            # -----------------------------------
            if node.isWord:
                res.add(word)

            # -----------------------------------
            # 5. Explore neighbors
            #    only up/down/left/right
            # -----------------------------------
            dfs(r + 1, c, node, word)  # down
            dfs(r - 1, c, node, word)  # up
            dfs(r, c + 1, node, word)  # right
            dfs(r, c - 1, node, word)  # left

            # -----------------------------------
            # 6. Backtrack
            # -----------------------------------

            # remove this cell from current path
            # so other DFS paths may use it later
            visit.remove((r, c))

        # -----------------------------------
        # 7. Start DFS from every board cell
        # -----------------------------------
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # convert set to list for final answer
        return list(res)