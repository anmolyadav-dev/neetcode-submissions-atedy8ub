# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.dfs(root)
        return self.res
    def dfs(self,root):
        if not root:
            return 
        if self.res:
            return 
        
        self.dfs(root.left)
        self.count +=1
        if self.count == k :
            self.res = root.val    
        self.dfs(root.right)
        
        

    
    
