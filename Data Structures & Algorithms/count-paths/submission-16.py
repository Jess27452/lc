class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [0] * n
        row[-1] = 1
        # if write like this then this is not the bottom row since all others we filled as 0 here

        for i in range(m):

            newrow = [1] * n

            for a in range(n - 2, -1, -1):
                newrow[a] = newrow[a + 1] + row[a]

            row = newrow

        return row[0]