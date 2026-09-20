# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self,
        root: TreeNode,
        target: int
    ) -> TreeNode:

        stack = [root]
        parents = {root: None}
        visited = set()

        while stack:
            node = stack.pop()

            # If node is currently a leaf
            if not node.left and not node.right:
                if node.val == target:
                    parent = parents[node]

                    # The root itself must be deleted
                    if not parent:
                        return None

                    # Disconnect node from its parent
                    if parent.left == node:
                        parent.left = None

                    if parent.right == node:
                        parent.right = None

            # Node is not a leaf and its children
            # have not been processed yet
            elif node not in visited:
                visited.add(node)

                # Put node back so it is processed
                # again after its children
                stack.append(node)

                if node.left:
                    parents[node.left] = node
                    stack.append(node.left)

                if node.right:
                    parents[node.right] = node
                    stack.append(node.right)

        return root  