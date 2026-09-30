class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei=collections.defaultdict(list)
        #Without adding "hit" when building nei, the pattern dictionary might not contain "hit" as one of the words for h*t.
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit=set([beginWord])
        q=deque([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res+=1
        return 0
