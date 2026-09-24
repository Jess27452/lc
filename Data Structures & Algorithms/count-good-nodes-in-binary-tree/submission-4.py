# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_Val):
            if not node:
                return 0
            if node.val>=max_Val:
                count=1
            else:
                count=0
            max_Val=max(node.val,max_Val)
            left=dfs(node.left,max_Val)
            right=dfs(node.right,max_Val)
            return left+right+count
        return dfs(root,root.val)
            