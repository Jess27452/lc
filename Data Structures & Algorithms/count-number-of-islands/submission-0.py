import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, there are no islands
        if not grid:
            return 0

        # Number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # visit = set of cells we have already discovered
        # Example: {(0,0), (0,1), (1,0)}
        visit = set()

        # Final answer: how many separate islands we found
        islands = 0

        # ---------------------------------------------------
        # BFS function:
        # Starts from one land cell (r, c)
        # and explores the ENTIRE island connected to it
        # ---------------------------------------------------
        def bfs(r, c):
            # Queue for BFS
            q = collections.deque()

            # VERY IMPORTANT:
            # The moment we start from (r, c),
            # we do TWO things immediately:
            #
            # 1. add to visit -> mark as discovered
            # 2. add to q     -> schedule it to be explored
            #
            # Why both now?
            # Because once we discover a cell, we do not want
            # to add it again later from another direction.
            visit.add((r, c))
            q.append((r, c))

            # Keep exploring until there are no more cells left
            # in this island's BFS queue
            while q:
                # Take the next cell from the front of the queue
                row, col = q.popleft()

                # Check the 4 directions only:
                # down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    # Compute neighbor coordinate
                    nr, nc = row + dr, col + dc

                    # We only add neighbor if:
                    # 1. it is inside the grid
                    # 2. it is land ("1")
                    # 3. it has NOT been visited yet
                    if (
                        nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visit
                    ):
                        # VERY IMPORTANT:
                        # The moment we DISCOVER this neighbor,
                        # we again do TWO things immediately:
                        #
                        # 1. add to queue
                        # 2. add to visit
                        #
                        # q.append(...) means:
                        #   "explore this cell later"
                        #
                        # visit.add(...) means:
                        #   "we already know about this cell,
                        #    so don't add it again later"
                        q.append((nr, nc))
                        visit.add((nr, nc))

        # ---------------------------------------------------
        # Scan every cell in the grid
        # ---------------------------------------------------
        for r in range(rows):
            for c in range(cols):
                # If this cell is land and NOT visited,
                # it means we found a brand new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Explore the whole island
                    bfs(r, c)

                    # Count this island once
                    islands += 1

        # Return total number of islands
        return islands