# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(
        self,
        root: Optional[TreeNode],
        key: int
    ) -> Optional[TreeNode]:

        if not root:
            return None

        # Search in the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Search in the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Found the node to delete
        else:
            # No left child
            if not root.left:
                return root.right

            # No right child
            if not root.right:
                return root.left

            # Two children:
            # Find the smallest node in the right subtree
            cur = root.right

            while cur.left:
                cur = cur.left

            # Replace root's value with successor's value
            root.val = cur.val

            # Delete the duplicate successor node
            root.right = self.deleteNode(root.right, cur.val)

        return root