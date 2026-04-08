# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMin(self,root: Optional[TreeNode]):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        

        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        
        else:

            #case1: only either of left/right exists or is leafnode
            if not root.left :
                return root.right
            elif not root.right:
                return root.left
            
            # case2: both exists
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val #added min from right subtreein place of one to remove
                #remove min from bottom
                root.right = self.deleteNode(root.right,minNode.val)
        return root


        