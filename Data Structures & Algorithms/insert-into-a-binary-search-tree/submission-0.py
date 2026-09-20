# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(
        self,
        root: Optional[TreeNode],
        val: int
    ) -> Optional[TreeNode]:

        # Empty tree: the new node becomes the root
        if not root:
            return TreeNode(val)

        cur = root

        while True:
            if val > cur.val:
                # The value belongs on the right
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root

                cur = cur.right
#1. Find an empty position
#2. Insert the new node
#3. Execute return root
#4. Exit insertIntoBST completely
            else:
                # The value belongs on the left
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root

                cur = cur.left  