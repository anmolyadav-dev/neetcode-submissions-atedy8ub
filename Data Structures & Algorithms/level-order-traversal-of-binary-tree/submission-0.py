# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        if not root:
            return []
        queue.append(root)
        level = -1
        while(queue):
            level = level + 1
            res.append([])
            qlen = len(queue)
            for i in range(qlen):
                top = queue.popleft()
                res[level].append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
        return res
