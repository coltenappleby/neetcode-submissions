# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS, preorder, but we need to keep track of a max value

        stack = [(root, -101)]
        node = root
        res = 0

        while stack:
            node, parent_max = stack.pop()
            if node.val >= parent_max:
                res += 1
            max_parent = max(node.val, parent_max)
            if node.right:
                stack.append((node.right, max_parent))
            if node.left:
                stack.append((node.left, max_parent))
        return res
            

            
            
            
