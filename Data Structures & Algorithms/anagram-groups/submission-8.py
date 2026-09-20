class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for s in strs:
            keys=''.join(sorted(s))
            if keys not in group:
                group[keys]=[]
            group[keys].append(s)
        return list(group.values())