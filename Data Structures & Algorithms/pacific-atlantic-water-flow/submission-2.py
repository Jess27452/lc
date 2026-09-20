class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # number of rows and columns
        ROWS, COLS = len(heights), len(heights[0])

        # pac = cells that can reach Pacific
        # atl = cells that can reach Atlantic
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):# the vist here refers to the pac and atl set
            # stop if:
            # 1. out of bounds
            # 2. already visited for this ocean
            # 3. current cell is too low for reverse flow
            if ((r, c) in visit or
                r < 0 or c < 0 or r == ROWS or c == COLS or
                heights[r][c] < prevHeight):#reverse DFS from moving downhill
                return

            # mark current cell reachable by this ocean
            visit.add((r, c))

            # continue DFS in 4 directions
            # next cells must have height >= current height
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # top row = Pacific border
        # bottom row = Atlantic border
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])# run the row

        # left column = Pacific border
        # right column = Atlantic border
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])# run the column

        # collect cells reachable by both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])# geenrate reuslst

        return res
        #I reverse the flow direction and run two traversals from the ocean borders inward, moving only to equal-or-higher cells. One traversal marks cells that can reach the Pacific, the other marks cells that can reach the Atlantic, and the intersection of those two sets is the answer.