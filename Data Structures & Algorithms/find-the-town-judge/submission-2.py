class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        tl={i:[] for i in range(n+1)}
        bl={i:[] for i in range(n+1)}
        for a, b in trust:
            tl[a].append(b)
            bl[b].append(a)
        for i in range (n+1):
            if len(bl[i])==n-1 and len(tl[i])==0:
                return i
        return -1

