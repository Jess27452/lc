from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in wordList, impossible
        if endWord not in wordList:
            return 0

        nei = defaultdict(list)

        # Add beginWord because it may not be in wordList
        wordList.append(beginWord)

        # Build pattern dictionary
        # Example: "cat" -> "*at", "c*t", "ca*"
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        # BFS
        while q:
            # Process one level at a time
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                # Try all patterns of current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    # Find all neighbor words with same pattern
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            # Finished one transformation level
            res += 1

        return 0