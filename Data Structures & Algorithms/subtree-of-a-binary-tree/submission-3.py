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

    def sameTree(self, s, t):
        # Both positions are empty
        if not s and not t:
            return True

        # Both nodes exist and have the same value
        if s and t and s.val == t.val:
            return (
                self.sameTree(s.left, t.left)
                and self.sameTree(s.right, t.right)
            )

        return False