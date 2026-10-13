class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            # Assume the current square is uniform
            all_same = True

            # Check every cell in the current square
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False
                        break

                if not all_same:
                    break

            # BASE CASE:
            # Return one leaf node if all values match
            if all_same:
                return Node(
                    grid[r][c],
                    True,
                    None, None, None, None
                )

            # RECURSIVE CASE:
            # Divide the square into 4 smaller squares
            half = n // 2

            # Each dfs returns the root of a subtree
            top_left = dfs(half, r, c)
            top_right = dfs(half, r, c + half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r + half, c + half)

            # Connect the four returned subtrees
            # under one new parent node
            return Node(
                1,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        # Return the root of the entire Quad Tree
        return dfs(len(grid), 0, 0)