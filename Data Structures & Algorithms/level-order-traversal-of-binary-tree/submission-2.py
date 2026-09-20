# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #enqueue:  add to back
#dequeue:  remove from front

        if not root:
            return []
        
        res = []
        queue = deque([root])#it only adds root

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()#popleft 最左边的#pop ispoping the left
                level.append(node.val)

                if node.left:
                    queue.append(node.left)#here we add queue
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res