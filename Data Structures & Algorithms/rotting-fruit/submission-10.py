class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q=collections.deque()
        fresh = 0
        time = 0
        visit=set()
        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r,c))
        def addOrange(r,c):
            nonlocal fresh
            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c]!=1 or (r,c) in visit):
                return
            q.append((r,c))
            visit.add((r,c))
            fresh-=1
        time=0
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                addOrange(r+1,c)
                addOrange(r,c+1)
                addOrange(r-1,c)
                addOrange(r,c-1)
            time+=1
        return time if fresh==0 else -1


