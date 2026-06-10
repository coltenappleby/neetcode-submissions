# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        def dfs(node, min_value, max_value) -> bool:
            if not node:
                return True
            
            if not min_value < node.val < max_value:
                return False
            
            left_side = dfs(node.left, min_value, node.val)
            right_side = dfs(node.right, node.val, max_value)

            return left_side and right_side

        return dfs(root, float("-inf"), float("inf"))
            
