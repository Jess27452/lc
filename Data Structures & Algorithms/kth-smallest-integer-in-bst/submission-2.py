# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###########this is inorder using stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left#smallest always on the left
                #keep going LEFT to find smaller values
            curr = stack.pop()
            #left subtree finished,
#now visit this node
            k -= 1
            if k == 0:
                return curr.val# if the number is not equal to k then 
                # we can go to its right since even it's right, the right is
                #still smaller than its root
        
            curr = curr.right
            #after Left and Root,
#go process Right subtree

########using iterative stack method 1. To avoid recursion depth problems