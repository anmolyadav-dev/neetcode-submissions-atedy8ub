# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        queue = deque()
        lvl = -1

        if root :
            queue.append(root)
        
        while queue:
            lvl +=1 
            traversal.append([])
            ln = len(queue)
            for i in range(ln):
                el = queue.popleft()
                if el: 
                    traversal[lvl].append(el.val)
                if el.left: queue.append(el.left)
                if el.right: queue.append(el.right)
        res = []
        for i in traversal:
            res.append(i[-1])

        return res


