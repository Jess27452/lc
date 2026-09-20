class TrieNode:
    def __init__(self):
        # children maps a character to the next TrieNode
        # example: {'d': node1, 'b': node2}
        self.children = {}

        # True if a full word ends at this node
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        # root is the starting node of the trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # start at the root
        cur = self.root

        # go through each character in the word
        for c in word:
            # if this character path does not exist yet, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # move cur to the child for this character
            cur = cur.children[c]

        # after the last character, mark this node as the end of a word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # dfs(i, node) means:
        # can we match word[i:] starting from this trie node?
        def dfs(i, node):
            # start this search from the given node
            cur = node

            # loop through the word starting at index i
            for j in range(i, len(word)):
                c = word[j]

                # if current character is '.', it can match any one letter
                if c == ".":
                    # try every possible child
                    for child in cur.children.values():
                        # if any child matches the rest of the word, return True
                        if dfs(j + 1, child):
                            return True

                    # if none of the children work, return False
                    return False

                # if current character is a normal letter,
                # that letter must exist in cur.children
                if c not in cur.children:
                    return False

                # move to the next trie node for this character
                cur = cur.children[c]

            # if we finished all characters,
            # this is only a valid match if a full word ends here
            return cur.endOfWord

        # start searching from index 0 at the root
        return dfs(0, self.root)