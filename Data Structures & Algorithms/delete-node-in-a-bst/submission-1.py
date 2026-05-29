# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # RETURNS NEW (OR OLD) ROOT OF THE TREE

        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 0 Childs
            if root.left == None and root.right == None:
                return None

            # 1 Child
            elif root.left != None and root.right == None:
                return root.left
            elif root.right != None and root.left == None:
                return root.right

            # 2 Childs
            else:
                smallest = self.findMinimum(root.right)
                root.val = smallest.val
                root.right = self.deleteNode(root.right, smallest.val)
                
        return root

    def findMinimum(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

        