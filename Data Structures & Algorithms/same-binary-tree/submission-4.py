# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both positions are empty
        if not p and not q:
            return True

        # One is empty, or their values are different
        if not p or not q or p.val != q.val:
            return False

        # Left subtrees and right subtrees must both match
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )    