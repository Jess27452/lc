from collections import defaultdict


class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: list[list[int]],
        colConditions: list[list[int]]
    ) -> list[list[int]]:

        def topo_sort(edges):
            # Build graph
            adj = defaultdict(list)

            for src, dst in edges:
                adj[src].append(dst)

            visit = set()
            path = set()
            order = []

            def dfs(src):
                # Already in current DFS path -> cycle
                if src in path:
                    return False

                # Already completely processed
                if src in visit:
                    return True

                visit.add(src)
                path.add(src)

                for nei in adj[src]:
                    if not dfs(nei):
                        return False

                path.remove(src)

                # Add after processing neighbors
                order.append(src)

                return True

            # We need every number from 1 to k
            for src in range(1, k + 1):
                if not dfs(src):
                    return []

            # Reverse because DFS adds nodes backwards
            return order[::-1]

        # Get valid row ordering
        row_order = topo_sort(rowConditions)

        # Get valid column ordering
        col_order = topo_sort(colConditions)

        # If either has a cycle, impossible
        if not row_order or not col_order:
            return []

        # Map each number to its row
        val_to_row = {
            num: i
            for i, num in enumerate(row_order)
        }

        # Map each number to its column
        val_to_col = {
            num: i
            for i, num in enumerate(col_order)
        }

        # Create k x k matrix filled with 0
        res = [
            [0] * k
            for _ in range(k)
        ]

        # Put every number in its row + column
        for num in range(1, k + 1):
            r = val_to_row[num]
            c = val_to_col[num]

            res[r][c] = num

        return res