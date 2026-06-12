"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        newNode = Node()
        def dfs(node):
            if node and node in oldToNew: return oldToNew[node]
            

            clone = Node(node.val)
            
            oldToNew[node] = clone
            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))
            return clone
        if not node : return 
        return dfs(node)
        

