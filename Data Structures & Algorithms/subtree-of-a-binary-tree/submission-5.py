# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node,sub):
            if not sub and not node:
                return True
            if not node or not sub or node.val!= sub.val:
                return False;
            
            
            return  dfs(node.left,sub.left) and dfs(node.right,sub.right)
                
        if not subRoot:
            return True
        if not root:
            return False
        if dfs(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            