# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:

        cur = root

        while cur:
            # Both target nodes are larger,
            # so they must be in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            # Both target nodes are smaller,
            # so they must be in the left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # p and q split into different directions,
            # or cur is equal to p or q.
            else:
                return cur