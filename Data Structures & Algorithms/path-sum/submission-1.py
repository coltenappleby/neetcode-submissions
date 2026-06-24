# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        tot = 0
        
        def backTracking(node, tot):
            if not node: #or not node.val:
                return False

            tot += node.val

            if not node.right and not node.left and tot == targetSum:
                print("Made it", tot)
                return True

            print(node.val, tot)
            if backTracking(node.left, tot):
                return True
            if backTracking(node.right, tot):
                return True
            tot -= node.val

            return False
        return backTracking(root, tot)
        
