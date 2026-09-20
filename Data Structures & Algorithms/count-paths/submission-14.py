class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n
        for i in range(m-1):
            newrow=[0]*n
            newrow[-1]=1
            for a in range (n-2,-1,-1):
                newrow[a]=newrow[a+1]+row[a]
            row=newrow
        return row[0]
