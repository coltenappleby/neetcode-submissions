# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # return p == q
        if p == None and q == None:
            return True

        if p == None and q != None or p != None and q == None:
            return False

        # if p.left == None and p.right == None and q.left == None and q.right == None:
        #     return p.val == q.val


        if  p.val != q.val:
            return False

        left_child = self.isSameTree(p.left, q.left)
        right_child = self.isSameTree(p.right, q.right)

        if not left_child or not right_child:
            return False
        else:
            return True

        

        