# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)     # 1 go left
            
            self.k -= 1            # 2 visit node
            if self.k == 0:
                self.ans = node.val
                return
            
            inorder(node.right)    # 3 go right

        inorder(root)
        return self.ans