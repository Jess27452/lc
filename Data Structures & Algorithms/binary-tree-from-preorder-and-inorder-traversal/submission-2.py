# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
#If mid = 1, then:

#preorder[1:2]

#which gives one element
    # base case: no nodes left
        if not preorder or not inorder:
            return None

        # first value in preorder is the root
        root = TreeNode(preorder[0])

        # find root position in inorder
        mid = inorder.index(preorder[0])

        # build left subtree
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # build right subtree
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
