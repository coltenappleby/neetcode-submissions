# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # start time 9:39 am
        # get to bottom of tree
        # move up, and swithc right node and left node

        if root == None:
            return root
        
        oldLeft = root.left
        if root.right != None:
            root.left = self.invertTree(root.right)
        else:
            root.left = None
        if oldLeft != None:     
            root.right = self.invertTree(oldLeft)
        else:
            root.right = None

        return root