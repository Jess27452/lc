"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            all_same = True

            # Check whether every cell in this n × n square
            # has the same value as grid[r][c].
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break

                if not all_same:
                    break

            # Base case: this entire square has one value.
            if all_same:
                return Node(grid[r][c], True)

            half = n // 2

            # Otherwise, divide the square into four parts.
            top_left = dfs(half, r, c)
            top_right = dfs(half, r, c + half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r + half, c + half)

            return Node(
                1,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return dfs(len(grid), 0, 0)