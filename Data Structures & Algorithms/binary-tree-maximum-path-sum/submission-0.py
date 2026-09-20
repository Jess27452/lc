# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       #Preorder

#In preorder, the first element is always the root of the current tree.
# this is the preorder, inoorder psote oder question

        self.best = float("-inf")

        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_path = node.val + left_gain + right_gain
            self.best = max(self.best, current_path)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best