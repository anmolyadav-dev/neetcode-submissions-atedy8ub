# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        ans = 0
        def dfs(node):
            nonlocal res
            nonlocal ans
            if not node:
                return 
            if dfs(node.left):
                return
            ans+=1
            if ans == k:
                res = node.val
                return True
            if dfs(node.right):
                return 
        dfs(root)
        return res