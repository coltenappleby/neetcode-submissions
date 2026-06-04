# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # pre-order
        # there should be a way to do this with breadth-first 

        locations = {}

        node = root
        stack = []
        depth = 0

        while stack or node:
            if node:
                stack.append((depth, node))
                if depth not in locations:
                    locations[depth] = node.val
                depth += 1
                node = node.right
            else:
                depth, node = stack.pop()
                node = node.left
                depth += 1
        print(locations)
        return list(locations.values())
