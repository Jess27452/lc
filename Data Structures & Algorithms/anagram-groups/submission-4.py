from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # count[0] represents 'a', count[1] represents 'b', etc.
            count = [0] * 26

            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1

            # Lists cannot be dictionary keys, so convert count to a tuple.
            res[tuple(count)].append(s)

        return list(res.values())