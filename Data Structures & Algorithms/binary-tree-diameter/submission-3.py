# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # Returns the height of curr
        def dfs(curr):
            nonlocal res

            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # Longest path that passes through curr
            res = max(res, left + right)

            # Height of the current subtree
            return 1 + max(left, right)

        dfs(root)
        return res