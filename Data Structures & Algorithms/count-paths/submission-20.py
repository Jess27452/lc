class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[0]*n
        row[-1]=1
        for i in range(m):
            for j in range(n-2,-1,-1):
                row[j]=row[j+1]+row[j]
        return row[0]
