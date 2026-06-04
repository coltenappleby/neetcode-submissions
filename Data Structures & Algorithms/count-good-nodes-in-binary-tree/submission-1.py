# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        

        def preorder(node, parent_max: int) -> int:
            if not node:
                return 0

            node_max = max(node.val, parent_max)

            count_left = preorder(node.left, node_max)
            count_right = preorder(node.right, node_max)

            children_count = count_left + count_right

            if node.val >= parent_max:
                children_count += 1
            return children_count

        return preorder(root, -101)

