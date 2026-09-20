class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                b=ord(c)-ord("a")
                count[b]+=1
            res[tuple(count)].append(s)
                #cannot use 'list' as a dict key (unhashable type: 'list')
        return list(res.values())