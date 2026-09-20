class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows=[1]*n
        for _ in range(m-1):
            new_row=[0]*n
            new_row[-1]=1
            for j in range(n-2,-1,-1):
                 new_row[j]=new_row[j+1]+rows[j]
            rows=new_row
        return rows[0]
            