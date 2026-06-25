# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, tot):
            if not node:
                return False

            tot += node.val # 1 => 

            if not node.left and not node.right and tot == targetSum:
                return True
            
            if dfs(node.left, tot):
                return True
            if dfs(node.right, tot):
                return True
            tot -= node.val
            return False

        return dfs(root, 0)
        