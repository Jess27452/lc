# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root):
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            for _ in range(qLen):
                node = q.popleft()

                if node:#Suppose node 9 is a leaf:

 #   9
  # / \
#None None

#The code still runs:

#q.append(node.left)   # appends None
#q.append(node.right)  # appends None
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res      