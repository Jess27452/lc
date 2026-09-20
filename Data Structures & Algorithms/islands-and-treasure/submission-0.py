from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):#Try adding neighboring room into queue
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visit or
                grid[r][c] == -1
            ):
                return

            visit.add((r, c))
            q.append((r, c))

        # Step 1: put all treasure cells into queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0

        # Step 2: BFS from all treasures at the same time
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                #it finishes first layer(dist 0)(every dist 0) and then go to the dist 1
#BFS starts to process all treasures using this  for i in range(len(q)):
#Now:

#for i in range(2)

#FINISHES.

#Even though queue has new items:

#[(0,1), (0,2)]

#they are NOT processed yet.
                addRoom(r + 1, c)# this is not recursion justc alling other fucntiosn
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1