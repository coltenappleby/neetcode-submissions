"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        def dfs(node, nodes):
            if node in nodes:
                return nodes[node]
            res = Node(node.val, None)
            nodes[node] = res 

            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor, nodes)
                res.neighbors.append(neighbor_copy)
            
            
            return res
        return dfs(node, {})
