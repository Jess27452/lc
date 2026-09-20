# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> TreeNode:

        # No nodes remain for this subtree.
        if not preorder or not inorder:
            return None

        # The first preorder value is always the root.
        root = TreeNode(preorder[0])

        # Find the root's position in inorder.
        mid = inorder.index(preorder[0])

        # Build the left and right subtrees.
        root.left = self.buildTree(
            preorder[1 : mid + 1],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid + 1 :],
            inorder[mid + 1 :]
        )

        return root