# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        queue = deque()
        res = []

        if not root:
            return res

        queue.append(root)
        
        while queue: # and root?
            queue_len = len(queue)

            for i in range(queue_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i+1 == queue_len:
                    res.append(node.val)
                
        return res




        