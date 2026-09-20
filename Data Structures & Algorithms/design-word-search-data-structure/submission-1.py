class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        #for example".ay"
                        #first cur=self.root
                        #cur.chidlren,value() can be {'d':NodeD;'c':NodeC...}
                        #try each one
                        if dfs(i + 1, child):# if children match the remaining
                        #character in c, then return true
                            return True
                    return False
#At ".", try one child deeply.
#If it works → done.
#If not → backtrack and try another child.
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word

        return dfs(0, self.root)