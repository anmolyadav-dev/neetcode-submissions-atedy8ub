# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = deque()
        q.append((root,root))

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node[0].val >= node[1].val:
                    ans+=1
                    if node[0].left :
                        q.append((node[0].left,node[0]))
                    if node[0].right:
                        q.append((node[0].right,node[0]))
                else:

                    if node[0].left :
                        q.append((node[0].left,node[1]))
                    if node[0].right:
                        q.append((node[0].right,node[1]))
        
        return ans

        
        