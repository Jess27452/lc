# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        pval, qval = p.val, q.val
        
        while cur:
            if pval < cur.val and qval < cur.val:
                cur = cur.left
            elif pval > cur.val and qval > cur.val:
                cur = cur.right
            else:
                return cur#this is where the split happens, for example
                # if one value is alrger and one value is smaller than current
                # value
                #or when one value equals to this current value