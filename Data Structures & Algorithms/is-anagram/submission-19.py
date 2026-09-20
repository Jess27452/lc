class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts,countt={},{}
        for i,m in zip(s,t):
            counts[i]=counts.get(i,0)+1
            countt[m]=countt.get(m,0)+1
        return counts==countt
            