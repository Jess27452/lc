# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)
        rh=root
        while q:
            rh=None
            level=[]
            for i in range(len(q)):
                cur=q.popleft()
                if cur:
                    rh=cur.val
                    q.append(cur.left)
                    q.append(cur.right)
            if rh is not None:
                res.append(rh)
        return res
            