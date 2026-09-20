# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def postorderTraversal(
        self,
        root: Optional[TreeNode]
    ) -> List[int]:

        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur = stack.pop()
            v = visit.pop()

            if cur:
                if v:
                    res.append(cur.val)
                else:
                    # Process this node after its children
                    stack.append(cur)
                    visit.append(True)

                    # Save right child
                    stack.append(cur.right)
                    visit.append(False)

                    # Save left child
                    stack.append(cur.left)
                    visit.append(False)

        return res  