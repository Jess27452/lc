# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True

        if not s:
            return False

        # Check whether the tree beginning at s is exactly t
        if self.sameTree(s, t):
            return True

        # Otherwise, search for t inside s's left or right subtree
        return (
            self.isSubtree(s.left, t)
            or self.isSubtree(s.right, t)
        )

    def sameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both positions are empty
        if not p and not q:
            return True

        # One is empty, or their values are different
        if not p or not q or p.val != q.val:
            return False

        # Left subtrees and right subtrees must both match
        return (
            self.sameTree(p.left, q.left)
            and self.sameTree(p.right, q.right)
        )    