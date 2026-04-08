# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root)
    def dfs(self,node,par):
        if not node : return 0
        if node.val >= par.val:
            return 1 + self.dfs(node.left,node) + self.dfs(node.right,node)
        else:
            return 0 + self.dfs(node.left,par) + self.dfs(node.right,par)
