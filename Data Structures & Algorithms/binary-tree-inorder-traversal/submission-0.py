# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root.right == None and root.left == None:
        if not root:
            # base case
            return []

        order = []

        left_order = self.inorderTraversal(root.left)
        if left_order:
            order.extend(left_order)

        order.append(root.val)

        right_order = self.inorderTraversal(root.right)
        if right_order:
            order.extend(right_order)

        return order
