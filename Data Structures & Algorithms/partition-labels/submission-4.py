class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i,v in enumerate(s):
            lastindex[v]=i
        res=[]
        size=0
        end=0
        for i,v in enumerate(s):
            size+=1
            end=max(end,lastindex[v])
            if i ==end:
                res.append(size)
                size=0
        return res
        