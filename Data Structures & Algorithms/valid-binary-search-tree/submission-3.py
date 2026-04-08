# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print(root.val,root.left.val if root.left else None,root.right.val if root.right else None)
        return self.isValid(root,-1000,1000)
    

    def isValid(self,root,mini,maxi):
        # print(root.val,mini,maxi)
        if root.val <= mini or root.val >= maxi:
            return False
        if root.left and root.right:
            return self.isValid(root.left,mini,root.val) and self.isValid(root.right,root.val,maxi)
        elif root.left :
            return  self.isValid(root.left,mini,root.val)
        
        elif root.right :
            return self.isValid(root.right,root.val,maxi)
        
        else : return True
        
            

    

