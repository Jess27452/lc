# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return [0, 0]

            left_pair = dfs(node.left)
            right_pair = dfs(node.right)

            # Rob the current node:
            # we must NOT rob its direct children.
            with_node = (
                node.val
                + left_pair[1]
                + right_pair[1]
            )

            # Do not rob the current node:
            # for each child, choose its better possibility.
            without_node = (
                max(left_pair)
                + max(right_pair)
            )

            return [with_node, without_node]

        return max(dfs(root))