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

        if p.left == None and p.right == None and q.left == None and q.right == None:
            return p.val == q.val

        left_child = True
        if p.left != None and q.left != None:
            left_child = self.isSameTree(p.left, q.left)
        elif (p.left != None and q.left == None) or (p.left == None and q.left != None):
            return False # exit early 
        # else is they are both None and left_child = True

        right_child = True
        if p.right != None and q.right != None:
            right_child = self.isSameTree(p.right, q.right)
        elif (p.right != None and q.left == None) or (p.right == None and q.right != None):
            return False

        return p.val == q.val and left_child and right_child

        

        