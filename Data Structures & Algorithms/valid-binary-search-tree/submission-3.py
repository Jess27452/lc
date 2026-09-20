# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            # An empty tree is valid.
            if not node:
                return True

            # The current value must stay inside
            # its allowed range.
            if not (left < node.val < right):
                return False

            # Left child must be smaller than node.val.
            # Right child must be greater than node.val.
            return (
                valid(node.left, left, node.val)
                and
                valid(node.right, node.val, right)
            )

        return valid(root, float("-inf"), float("inf"))   