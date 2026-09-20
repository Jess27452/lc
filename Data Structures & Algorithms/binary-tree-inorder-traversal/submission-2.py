# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        res = []
        stack = []
        cur = root

        while cur or stack:

            # Go as far left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            # No more left nodes, so process the latest node
            cur = stack.pop()
            res.append(cur.val)

            # Then explore its right subtree
            cur = cur.right

        return res