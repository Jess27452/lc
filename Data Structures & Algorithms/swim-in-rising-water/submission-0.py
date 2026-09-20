from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # N is the number of rows and columns.
        # The grid is always N x N.
        N = len(grid)

        # visited stores cells that have already been added
        # to the min-heap.
        #
        # Each cell is stored as:
        # (row, column)
        visited = set()

        # Each heap item is:
        # [minimum required water level, row, column]
        #
        # We start at the top-left cell (0, 0).
        # We must wait until the water reaches grid[0][0]
        # before we can stand on the starting cell.
        min_heap = [[grid[0][0], 0, 0]]

        # Mark the starting cell as visited.
        visited.add((0, 0))

        # Four possible directions:
        # right, left, down, up
        directions = [
            [0, 1],   # right
            [0, -1],  # left
            [1, 0],   # down
            [-1, 0]   # up
        ]

        # Continue while there are cells we can explore.
        while min_heap:
            # Remove the cell that currently requires
            # the smallest water level.
            required_time, row, col = heapq.heappop(min_heap)

            # If we reached the bottom-right cell,
            # required_time is the minimum possible answer.
            if row == N - 1 and col == N - 1:
                return required_time

            # Check all four neighboring cells.
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                # Skip the neighbor if:
                # 1. It is above the grid.
                # 2. It is left of the grid.
                # 3. It is below the grid.
                # 4. It is right of the grid.
                # 5. It has already been added to the heap.
                if (
                    new_row < 0
                    or new_col < 0
                    or new_row >= N
                    or new_col >= N
                    or (new_row, new_col) in visited
                ):
                    continue

                # Mark the neighbor so we do not add it again.
                visited.add((new_row, new_col))

                # The water level needed for the new path is
                # the highest elevation encountered so far.
                #
                # Example:
                # current required level = 5
                # next cell height = 3
                # max(5, 3) = 5
                #
                # current required level = 5
                # next cell height = 8
                # max(5, 8) = 8
                new_required_time = max(
                    required_time,
                    grid[new_row][new_col]
                )

                # Add the neighboring cell to the min-heap.
                heapq.heappush(
                    min_heap,
                    [new_required_time, new_row, new_col]
                )

        # The problem guarantees a path exists,
        # so this line normally will not be reached.
        return -1