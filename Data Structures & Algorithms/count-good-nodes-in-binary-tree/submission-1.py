# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            # We moved past a leaf node.
            if not node:
                return 0

            # Count the current node if it is at least
            # as large as every earlier node on its path.
            if node.val >= max_val:
                count = 1
            else:
                count = 0

            # Update the largest value seen on this path.
            new_max = max(max_val, node.val)

            # Add good nodes from both subtrees.
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)