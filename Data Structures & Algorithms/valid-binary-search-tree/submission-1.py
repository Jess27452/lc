# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):#if it's null it's valid
            if not node:
                return True # when reaching the bottom children, then their chidlren
                #are none, which will return true and true
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            # when passing node.val, low becomes that number next time

        return dfs(root, float("-inf"), float("inf"))